---
name: change-risk-review
description: "Review revision risks such as meaning drift and factual regression. / 审查修订引入的语义漂移与事实回退风险。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "⚠️"
    requires: {}
---

# change-risk-review

## Purpose / 目标

Assess revision risks by focusing on meaning drift, factual regressions, and tone mismatches.

聚焦语义漂移、事实回退和语气偏差，评估修订风险。

## When to use / 何时使用

- "Review risks in this revised version."
- "这次修改有没有引入风险？"
- "Check if edits changed intended meaning."

## Inputs / 输入

- source_text: required
- revised_text: required
- risk_profile: optional, legal or academic or general

## Output / 输出

- risk_findings: categorized risk list
- severity_map: critical or major or minor
- mitigation_steps: targeted rollback or rewrite suggestions

## Boundaries / 边界

- Do not assert facts that are not in source context.
- Flag unresolved ambiguity instead of guessing.
- Keep risk claims evidence-based.

## Execution Guidance / 执行指引

1. Compare semantic intent between versions.
2. Detect factual and logical inconsistencies.
3. Classify risk severity and confidence.
4. Provide mitigation actions with priority.

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
