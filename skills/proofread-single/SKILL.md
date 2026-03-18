---
name: proofread-single
description: "Proofread one paragraph with minimal meaning drift. / 单段精校，尽量不改变原意。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "✍️"
    requires: {}
---

# proofread-single

## Purpose / 目标

Deliver high-quality proofreading for short text while preserving tone, intent, and factual meaning.

对短文本进行高质量校对，保持语气、意图和事实含义不变。

## When to use / 何时使用

- "Please proofread this paragraph."
- "帮我润色这段，但不要改意思。"
- "Fix grammar and punctuation only."

## Inputs / 输入

- text: required, source paragraph
- style: optional, formal or natural
- strictness: optional, low or medium or high
- locale: optional, zh-CN or en

## Output / 输出

- revised_text: corrected text
- change_summary: short list of key fixes
- risk_notes: uncertain edits or factual risks

## Boundaries / 边界

- Do not invent facts.
- Do not over-rewrite unless strictness is high.
- If text is ambiguous, keep original and mark uncertainty.

## Execution Guidance / 执行指引

1. Detect language and writing register.
2. Correct spelling, grammar, punctuation, and obvious fluency issues.
3. Preserve named entities and factual statements.
4. Return revised text first, then concise summary.

## Prompt Contract / 提示约定

- Prioritize fidelity over style creativity.
- Keep response concise and actionable.
- If no change needed, state "No critical issues found".

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
