---
name: proofreading-decision-log
description: "Generate auditable logs for proofreading decisions. / 生成可审计的校对决策日志。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "📝"
    requires: {}
---

# proofreading-decision-log

## Purpose / 目标

Create a structured decision log that explains what was changed, why it was changed, and what risks remain.

生成结构化决策日志，说明改了什么、为什么改、剩余风险是什么。

## When to use / 何时使用

- "Create a proofreading decision log for this chapter."
- "把这次校对决策记录整理出来。"
- "Need an audit trail for edits."

## Inputs / 输入

- source_text: optional
- revised_text: optional
- diff_or_notes: required, change evidence
- audience: optional, editor or author or reviewer

## Output / 输出

- decision_entries: issue, decision, rationale, confidence
- unresolved_questions: items pending confirmation
- risk_register: impact and mitigation notes

## Boundaries / 边界

- Do not fabricate reasons not supported by evidence.
- Keep rationale concise and verifiable.
- Distinguish confirmed decision from tentative suggestion.

## Execution Guidance / 执行指引

1. Normalize change evidence into comparable units.
2. Summarize each decision with explicit rationale.
3. Add confidence and residual risk labels.
4. Output audit-ready structured log.
