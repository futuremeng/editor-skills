#!/usr/bin/env python3
"""Generate a markdown matrix for skills metadata and section coverage."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
OUTPUT = ROOT / "docs" / "skills-matrix.md"

CHECK_SECTIONS = [
    "## Purpose / 目标",
    "## Inputs / 输入",
    "## Output / 输出",
    "## Boundaries / 边界",
    "## Execution Guidance / 执行指引",
    "## Example I/O / 示例输入输出",
]


@dataclass
class SkillRow:
    name: str
    description: str
    section_score: str
    has_example: str


def extract_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[4:end], text[end + 5 :]


def extract_key(frontmatter: str, key: str) -> str:
    m = re.search(rf"(?:^|\n)\s*{re.escape(key)}\s*:\s*([^\n]+)", frontmatter)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'")


def build_rows() -> list[SkillRow]:
    rows: list[SkillRow] = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8")
        frontmatter, body = extract_frontmatter(text)
        name = extract_key(frontmatter, "name") or skill_dir.name
        description = extract_key(frontmatter, "description") or ""
        matched = sum(1 for section in CHECK_SECTIONS if section in body)
        has_example = "yes" if "## Example I/O / 示例输入输出" in body else "no"
        rows.append(
            SkillRow(
                name=name,
                description=description,
                section_score=f"{matched}/{len(CHECK_SECTIONS)}",
                has_example=has_example,
            )
        )
    return rows


def render_markdown(rows: list[SkillRow]) -> str:
    lines: list[str] = []
    lines.append("# Skills Matrix")
    lines.append("")
    lines.append("Auto-generated inventory of skill metadata and section coverage.")
    lines.append("")
    lines.append("自动生成的技能元数据与章节覆盖矩阵。")
    lines.append("")
    lines.append(f"Total skills: {len(rows)}")
    lines.append("")
    lines.append("| Skill | Description | Section Coverage | Example I/O |")
    lines.append("| --- | --- | --- | --- |")
    for row in rows:
        desc = row.description.replace("|", "\\|")
        lines.append(f"| {row.name} | {desc} | {row.section_score} | {row.has_example} |")
    lines.append("")
    lines.append("## Usage")
    lines.append("")
    lines.append("Regenerate this file with:")
    lines.append("")
    lines.append("python3 scripts/generate_skills_matrix.py")
    return "\n".join(lines) + "\n"


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills directory not found")
        return 2
    rows = build_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_markdown(rows), encoding="utf-8")
    print(f"Generated {OUTPUT} for {len(rows)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
