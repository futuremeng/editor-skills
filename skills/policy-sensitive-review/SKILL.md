---
name: policy-sensitive-review
description: "Flag policy and compliance sensitive expressions for human review. / 标注政策与合规敏感表达供人工复核。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🛡️"
    requires: {}
---

# policy-sensitive-review

## Purpose / 目标

Identify potentially sensitive policy, legal, or compliance-related statements and provide risk-aware rewrite suggestions.

识别潜在政策、法律或合规敏感表达，并给出风险感知的改写建议。

## When to use / 何时使用

- "Review this text for policy-sensitive risks."
- "帮我做合规敏感表达检查。"
- "Flag statements that need legal review."

## Inputs / 输入

- text: required
- context: optional, region or industry policy context
- risk_tolerance: optional, low or medium or high

## Output / 输出

- sensitive_findings: flagged expressions and risk rationale
- rewrite_options: conservative alternatives
- legal_review_needed: items that must go to human/legal review

## Boundaries / 边界

- This skill does not provide legal advice.
- Do not claim compliance certification.
- Escalate ambiguous high-risk statements for human review.

## Execution Guidance / 执行指引

1. Scan for policy or compliance-sensitive claims.
2. Classify risk level and explain triggers.
3. Provide cautious rewrite options.
4. Output clear escalation list for legal or compliance teams.
