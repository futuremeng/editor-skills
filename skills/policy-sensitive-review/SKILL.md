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
