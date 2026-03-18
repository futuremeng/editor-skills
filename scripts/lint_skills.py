#!/usr/bin/env python3
"""Lightweight linter for editor-skills SKILL.md files.

Supports severity levels (`error`/`warn`), JSON output, and strict warning mode.
"""

from __future__ import annotations

import argparse
import json
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


def collect_issues() -> tuple[list[Issue], int]:
    if not SKILLS_DIR.exists():
        return [Issue("error", "<repo>", "skills directory not found")], 0

    skill_dirs = sorted(
        d for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    )
    issues: list[Issue] = []
    for skill_dir in skill_dirs:
        issues.extend(lint_skill_file(skill_dir))
    return issues, len(skill_dirs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint SKILL.md files")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON output")
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="treat warnings as failure",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    issues, skill_count = collect_issues()

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
            print(f"Skill lint passed for {skill_count} skills.")

    if error_count > 0:
        return 1
    if args.strict_warnings and warn_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
