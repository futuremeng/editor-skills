---
name: chapter-quality-gate
description: "Apply acceptance gates before chapter sign-off. / 章节签发前质量闸门检查。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🚦"
    requires: {}
---

# chapter-quality-gate

## Purpose / 目标

Evaluate whether a chapter is ready for sign-off using explicit editorial gates.

基于明确的编辑闸门规则，判断章节是否可签发。

## When to use / 何时使用

- "Is this chapter ready to publish?"
- "这章能不能过稿？"
- "Run acceptance gate before final delivery."

## Inputs / 输入

- chapter_text: required
- gate_policy: optional, custom checklist
- quality_target: optional, baseline or strict

## Output / 输出

- gate_result: pass or conditional-pass or fail
- failed_checks: list with evidence
- remediation_plan: minimal fixes to pass

## Boundaries / 边界

- Do not output pass if critical checks fail.
- Distinguish blocking issues from suggestions.
- Keep criteria explicit and auditable.

## Execution Guidance / 执行指引

1. Evaluate language, consistency, structure, and risks.
2. Score against gate policy.
3. Generate fail reasons with direct evidence.
4. Provide shortest path to pass.

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
