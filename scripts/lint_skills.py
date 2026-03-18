#!/usr/bin/env python3
"""Lightweight linter for editor-skills SKILL.md files.

Supports severity levels (`error`/`warn`), JSON output, strict warning mode,
auto-fix of missing recommended sections, git-aware changed-only filtering,
and CI summary output.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

REQUIRED_FRONTMATTER_KEYS = [
    "name",
    "description",
    "metadata",
    "builtin_skill_version",
    "copaw",
    "emoji",
]

REQUIRED_SECTIONS = [
    "## Purpose / 目标",
    "## When to use / 何时使用",
    "## Inputs / 输入",
    "## Output / 输出",
    "## Boundaries / 边界",
    "## Execution Guidance / 执行指引",
    "## Example I/O / 示例输入输出",
]

RECOMMENDED_SECTIONS = [
    "## Prompt Contract / 提示约定",
]

# Default content appended by --fix for each recommended section
FIX_TEMPLATES: dict[str, str] = {
    "## Prompt Contract / 提示约定": (
        "\n## Prompt Contract / 提示约定\n\n"
        "- 保持建议的保守性和可追溯性。\n"
        "- 输出需注明信息来源或推断依据。\n"
        "- 如无法判断，优先标注\u300c待核查\u300d而非省略。\n"
        "- Keep recommendations conservative and traceable.\n"
        "- Annotate sources or reasoning behind each suggestion.\n"
        "- When uncertain, flag as 'pending review' rather than omitting.\n"
    ),
}


@dataclass
class Issue:
    severity: str  # error | warn
    skill: str
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    frontmatter = text[4:end]
    body = text[end + 5 :]
    return frontmatter, body


def lint_skill_file(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        issues.append(Issue("error", skill_dir.name, "missing SKILL.md"))
        return issues

    text = read_text(skill_file)
    frontmatter, body = extract_frontmatter(text)
    if not frontmatter:
        issues.append(Issue("error", skill_dir.name, "missing or malformed YAML frontmatter"))
        return issues

    for key in REQUIRED_FRONTMATTER_KEYS:
        if not re.search(rf"(^|\n)\s*{re.escape(key)}\s*:", frontmatter):
            issues.append(Issue("error", skill_dir.name, f"missing frontmatter key '{key}'"))

    name_match = re.search(r"(?:^|\n)name\s*:\s*([^\n]+)", frontmatter)
    if name_match:
        declared_name = name_match.group(1).strip().strip('"').strip("'")
        if declared_name != skill_dir.name:
            issues.append(
                Issue(
                    "error",
                    skill_dir.name,
                    f"frontmatter name '{declared_name}' does not match directory",
                )
            )

    for section in REQUIRED_SECTIONS:
        if section not in body:
            issues.append(Issue("error", skill_dir.name, f"missing section '{section}'"))

    for section in RECOMMENDED_SECTIONS:
        if section not in body:
            issues.append(Issue("warn", skill_dir.name, f"recommended section missing '{section}'"))

    return issues


def fix_skill_file(skill_dir: Path, issues: list[Issue]) -> list[str]:
    """Auto-append missing recommended sections. Returns list of fixed section names."""
    skill_file = skill_dir / "SKILL.md"
    fixed: list[str] = []
    for issue in issues:
        if issue.severity != "warn":
            continue
        for section, template in FIX_TEMPLATES.items():
            if issue.message == f"recommended section missing '{section}'":
                text = skill_file.read_text(encoding="utf-8")
                if section not in text:
                    skill_file.write_text(text.rstrip() + template, encoding="utf-8")
                    fixed.append(section)
    return fixed


def get_changed_skill_names() -> set[str]:
    """Return set of skill directory names that have uncommitted or staged changes."""
    changed_paths: set[str] = set()
    for cmd in (
        ["git", "diff", "--name-only", "HEAD"],
        ["git", "diff", "--cached", "--name-only"],
    ):
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=ROOT, timeout=10
            )
            changed_paths.update(result.stdout.splitlines())
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
    names: set[str] = set()
    for p in changed_paths:
        parts = Path(p).parts
        if len(parts) >= 2 and parts[0] == "skills":
            names.add(parts[1])
    return names


def collect_issues(changed_only: bool = False) -> tuple[list[Issue], int]:
    if not SKILLS_DIR.exists():
        return [Issue("error", "<repo>", "skills directory not found")], 0

    all_dirs = sorted(
        d for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    )

    if changed_only:
        changed_names = get_changed_skill_names()
        skill_dirs = [d for d in all_dirs if d.name in changed_names]
    else:
        skill_dirs = all_dirs

    issues: list[Issue] = []
    for skill_dir in skill_dirs:
        issues.extend(lint_skill_file(skill_dir))
    return issues, len(skill_dirs)


def write_ci_summary(
    path: Path, issues: list[Issue], skill_count: int, error_count: int, warn_count: int
) -> None:
    """Write a Markdown CI summary file."""
    lines = [
        "# Skill Lint Summary\n",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Skills checked | {skill_count} |",
        f"| Errors | {error_count} |",
        f"| Warnings | {warn_count} |",
        "",
    ]
    if issues:
        lines += [
            "## Issues\n",
            "| Severity | Skill | Message |",
            "|----------|-------|---------|",
        ]
        for i in issues:
            lines.append(f"| `{i.severity}` | `{i.skill}` | {i.message} |")
    else:
        lines.append(f"**All {skill_count} skills passed.**")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint SKILL.md files")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="treat warnings as failure",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="auto-append default content for missing recommended sections",
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="only lint skill files with uncommitted git changes",
    )
    parser.add_argument(
        "--ci-summary",
        metavar="FILE",
        help="write a Markdown CI summary to FILE (in addition to other output)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    issues, skill_count = collect_issues(changed_only=args.changed_only)

    # --fix: auto-repair warn issues before final reporting
    if args.fix:
        fix_map: dict[str, list[str]] = {}
        skill_dirs = {
            d.name: d
            for d in SKILLS_DIR.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()
        }
        for issue in list(issues):
            if issue.severity == "warn" and issue.skill in skill_dirs:
                fixed = fix_skill_file(skill_dirs[issue.skill], [issue])
                if fixed:
                    fix_map.setdefault(issue.skill, []).extend(fixed)
        if fix_map and not args.json:
            print("Auto-fixed:")
            for skill, sections in sorted(fix_map.items()):
                for s in sections:
                    print(f"  + {skill}: appended '{s}'")
        # re-lint after fixes
        issues, skill_count = collect_issues(changed_only=args.changed_only)

    error_count = sum(1 for i in issues if i.severity == "error")
    warn_count = sum(1 for i in issues if i.severity == "warn")

    if args.json:
        payload = {
            "skill_count": skill_count,
            "error_count": error_count,
            "warn_count": warn_count,
            "issues": [asdict(i) for i in issues],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if issues:
            print("Skill lint report:")
            for issue in issues:
                print(f"- [{issue.severity}] {issue.skill}: {issue.message}")
        else:
            label = f"{skill_count} skill(s)" if args.changed_only else f"{skill_count} skills"
            print(f"Skill lint passed for {label}.")

    if args.ci_summary:
        write_ci_summary(
            Path(args.ci_summary), issues, skill_count, error_count, warn_count
        )

    if error_count > 0:
        return 1
    if args.strict_warnings and warn_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
