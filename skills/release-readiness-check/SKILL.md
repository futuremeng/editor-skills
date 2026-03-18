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
