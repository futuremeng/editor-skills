---
name: terminology-consistency-check
description: "Check terminology consistency across sections. / 跨章节术语一致性检查。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "📎"
    requires: {}
---

# terminology-consistency-check

## Purpose / 目标

Detect inconsistent term usage and propose a canonical vocabulary set for editorial consistency.

识别术语使用不一致问题，并提供统一术语建议集。

## When to use / 何时使用

- "Check term consistency across this document."
- "帮我统一全文术语。"
- "Find inconsistent naming before final review."

## Inputs / 输入

- text_or_sections: required
- domain_glossary: optional, preferred terms
- strictness: optional, low or medium or high

## Output / 输出

- term_clusters: same-concept term groups
- canonical_candidates: recommended preferred forms
- replacement_plan: conservative replacement suggestions

## Boundaries / 边界

- Do not force replacement for direct quotes.
- Preserve brand names and legal names unless instructed.
- If confidence is low, mark as review-required.

## Execution Guidance / 执行指引

1. Extract candidate terms and aliases.
2. Cluster terms by semantic equivalence.
3. Rank canonical options by clarity and frequency.
4. Output replacements and exceptions.
