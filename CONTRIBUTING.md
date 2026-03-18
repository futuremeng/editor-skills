# Contributing to editor-skills

Thank you for contributing.

## Scope

This repository currently hosts prompt-only skills for editorial workflows.

## Skill Authoring Checklist

- Create one folder per skill under skills/.
- Folder name must be kebab-case.
- Add SKILL.md in each folder.
- Frontmatter name must equal folder name.
- Keep bilingual content aligned in meaning.
- Define input, output, boundaries, and execution guidance.
- Avoid executable scripts in current phase.

## Frontmatter Requirements

- name
- description
- metadata.builtin_skill_version
- metadata.copaw.emoji

## Review Rules

- Prefer minimal, conservative suggestions.
- Do not claim tool execution that did not happen.
- Keep output contract explicit and deterministic.

## Pull Request

- Explain why this skill is needed.
- Include one example trigger phrase in English and Chinese.
- Mention backward compatibility risks if any.

## Validation

- Run `python3 scripts/lint_skills.py` before submitting.
