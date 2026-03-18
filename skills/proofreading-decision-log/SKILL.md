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
