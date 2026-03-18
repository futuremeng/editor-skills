---
name: proofread-batch-plan
description: "Plan-only workflow for large proofreading tasks. / 大规模校对任务的规划型技能（不执行脚本）。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🗂️"
    requires: {}
---

# proofread-batch-plan

## Purpose / 目标

Create an execution plan for batch proofreading jobs without running tools or scripts.

为批量校对提供可执行计划，不直接调用脚本或外部工具。

## When to use / 何时使用

- "Plan proofreading for this whole manuscript."
- "给我一个批量校对流程。"
- "How should I split and review 50 chapters?"

## Inputs / 输入

- corpus_size: optional, chapter count or word count
- source_format: optional, markdown or txt or json
- constraints: optional, deadline, budget, review depth
- deliverable: optional, json report or markdown report

## Output / 输出

- phase_plan: step-by-step pipeline
- chunking_policy: segmentation strategy
- quality_gate: acceptance criteria per phase
- risk_controls: cost and consistency safeguards

## Boundaries / 边界

- Do not pretend to have executed any step.
- Do not claim API calls or file generation are complete.
- Keep plan realistic for human review loops.

## Execution Guidance / 执行指引

1. Estimate workload and propose chunk strategy.
2. Define per-chunk proofreading criteria.
3. Add review checkpoints and merge policy.
4. Provide rollback and exception handling steps.

## Prompt Contract / 提示约定

- Output in checklist form with clear sequence.
- Include assumptions explicitly.
- Provide a compact "ready to execute" summary.

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
