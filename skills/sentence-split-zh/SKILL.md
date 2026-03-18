---
name: sentence-split-zh
description: "Chinese sentence segmentation with stable numbering. / 中文句子切分与稳定编号。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🧵"
    requires: {}
---

# sentence-split-zh

## Purpose / 目标

Split Chinese text into sentence units that are suitable for alignment, diff, and proofreading review.

将中文文本切分为适合对齐、差异分析和校对的句子单元。

## When to use / 何时使用

- "Split this chapter into sentence list."
- "把这段按句子拆开并编号。"
- "Need sentence ids before alignment."

## Inputs / 输入

- text: required
- keep_paragraph: optional, true or false
- punctuation_mode: optional, strict or tolerant

## Output / 输出

- sentences: ordered list with sentence_id
- notes: merge or split decisions for tricky punctuation
- anomalies: suspiciously long or fragmented segments

## Boundaries / 边界

- Preserve original order.
- Keep quotations and parentheses coherent when possible.
- If segmentation confidence is low, flag it explicitly.

## Execution Guidance / 执行指引

1. Normalize punctuation variants.
2. Segment using sentence-ending punctuation and context cues.
3. Resolve edge cases such as abbreviations or nested quotes.
4. Return numbered sentences with concise notes.

## Prompt Contract / 提示约定

- Prefer stable split points over aggressive splitting.
- Keep output easy to map back to source text.

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
