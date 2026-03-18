#!/usr/bin/env python3
"""Lightweight linter for editor-skills SKILL.md files."""

from __future__ import annotations

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


def lint_skill_file(skill_dir: Path) -> list[str]:
    issues: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        issues.append(f"{skill_dir.name}: missing SKILL.md")
        return issues

    text = read_text(skill_file)
    frontmatter, body = extract_frontmatter(text)
    if not frontmatter:
        issues.append(f"{skill_dir.name}: missing or malformed YAML frontmatter")
        return issues

    for key in REQUIRED_FRONTMATTER_KEYS:
        if not re.search(rf"(^|\n)\s*{re.escape(key)}\s*:", frontmatter):
            issues.append(f"{skill_dir.name}: missing frontmatter key '{key}'")

    name_match = re.search(r"(?:^|\n)name\s*:\s*([^\n]+)", frontmatter)
    if name_match:
        declared_name = name_match.group(1).strip().strip('"').strip("'")
        if declared_name != skill_dir.name:
            issues.append(
                f"{skill_dir.name}: frontmatter name '{declared_name}' does not match directory"
            )

    for section in REQUIRED_SECTIONS:
        if section not in body:
            issues.append(f"{skill_dir.name}: missing section '{section}'")

    return issues


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills directory not found", file=sys.stderr)
        return 2

    skill_dirs = sorted(
        d for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    )
    all_issues: list[str] = []
    for skill_dir in skill_dirs:
        all_issues.extend(lint_skill_file(skill_dir))

    if all_issues:
        print("Skill lint failed:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print(f"Skill lint passed for {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
