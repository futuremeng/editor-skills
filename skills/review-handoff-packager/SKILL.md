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
