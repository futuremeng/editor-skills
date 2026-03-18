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
