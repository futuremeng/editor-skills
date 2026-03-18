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

## Example I/O / 示例输入输出

Input example:
- task: "Apply this skill to the provided text block"
- constraints: "Keep original intent and only apply necessary changes"

输入示例：
- 任务："对给定文本应用本技能"
- 约束："保持原意，仅做必要修改"

Output example:
- result: concise, structured outcome
- highlights: key findings and priority actions
- follow_up: unresolved items for human review

输出示例：
- 结果：结构化且简洁的处理结果
- 重点：关键发现与优先处理项
- 后续：需人工确认的未决事项

## Prompt Contract / 提示约定

- Keep recommendations conservative and traceable.
- Separate confirmed findings from uncertain assumptions.
- Preserve original intent unless explicit rewrite is requested.
- If confidence is low, provide options and mark review-required items.
