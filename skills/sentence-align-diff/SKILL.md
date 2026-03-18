---
name: sentence-align-diff
description: "Align source and revised sentences and summarize diffs. / 原文与修订文句级对齐并总结差异。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🔍"
    requires: {}
---

# sentence-align-diff

## Purpose / 目标

Produce a sentence-level alignment analysis between source and revised text with a human-readable diff summary.

对原文与修订文进行句级对齐，产出可读的差异摘要。

## When to use / 何时使用

- "Compare original and revised text."
- "请帮我对齐这两个版本并解释修改。"
- "Need insert delete replace summary."

## Inputs / 输入

- source_text: required
- revised_text: required
- granularity: optional, sentence or paragraph
- include_risk_tags: optional, true or false

## Output / 输出

- alignment_table: pair list with status (match replace insert delete)
- diff_summary: top change categories
- potential_regressions: meaning drift or factual risks

## Boundaries / 边界

- Do not claim exact algorithmic score if not computed.
- Preserve source order in analysis.
- Mark uncertain alignments explicitly.

## Execution Guidance / 执行指引

1. Segment both versions into aligned units.
2. Match units by semantic proximity and order.
3. Label changes as keep, replace, insert, delete.
4. Provide concise impact assessment.

## Prompt Contract / 提示约定

- Keep output deterministic and review-friendly.
- Highlight high-impact edits first.

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
