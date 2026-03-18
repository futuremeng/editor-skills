---
name: release-readiness-check
description: "Run pre-release editorial quality gates. / 执行发布前编辑质量总闸门检查。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "✅"
    requires: {}
---

# release-readiness-check

## Purpose / 目标

Provide a final go or no-go recommendation before publication using consolidated editorial gates.

基于汇总的编辑质量闸门，在发布前给出最终 go 或 no-go 建议。

## When to use / 何时使用

- "Is this document ready to release?"
- "发布前做一次总检查。"
- "Give final readiness verdict and blockers."

## Inputs / 输入

- document_or_report_pack: required
- gate_profile: optional, standard or strict
- risk_tolerance: optional, low or medium or high

## Output / 输出

- verdict: go or conditional-go or no-go
- blockers: critical issues with evidence
- release_checklist: last-mile actionable items

## Boundaries / 边界

- Do not output go when blockers remain unresolved.
- Distinguish blockers from non-blocking suggestions.
- Keep every blocker traceable to concrete evidence.

## Execution Guidance / 执行指引

1. Aggregate findings from consistency and risk checks.
2. Apply gate profile to classify severity.
3. Produce final verdict with explicit rationale.
4. Output shortest remediation path to go.

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
