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
