---
name: review-handoff-packager
description: "Package proofreading outcomes for editor-author handoff. / 打包校对结果用于编辑与作者交接。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "📦"
    requires: {}
---

# review-handoff-packager

## Purpose / 目标

Assemble a handoff package that helps editors and authors quickly understand changes, open questions, and next actions.

组装交接包，让编辑与作者快速理解改动、待确认问题和后续动作。

## When to use / 何时使用

- "Prepare a handoff package for the author."
- "给作者生成交接说明。"
- "Summarize this review cycle for team handoff."

## Inputs / 输入

- review_outputs: required, reports and notes
- target_reader: optional, author or PM or legal
- detail_level: optional, brief or standard or detailed

## Output / 输出

- executive_digest: high-level summary
- must_confirm_items: blocking questions for recipient
- action_backlog: prioritized tasks with owner hints

## Boundaries / 边界

- Do not hide critical blockers in summary.
- Keep traceability to source findings.
- Avoid adding unverifiable ownership claims.

## Execution Guidance / 执行指引

1. Aggregate findings by severity and topic.
2. Separate done items from pending confirmations.
3. Build recipient-focused action list.
4. Output concise handoff packet.

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
