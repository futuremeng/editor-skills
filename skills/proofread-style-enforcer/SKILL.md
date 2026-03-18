---
name: proofread-style-enforcer
description: "Enforce writing style guide while preserving meaning. / 在保留原意前提下执行文风规范。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🎯"
    requires: {}
---

# proofread-style-enforcer

## Purpose / 目标

Apply style-guide rules consistently to improve readability and publication alignment without changing factual meaning.

在不改变事实含义的前提下，统一执行文风规范，提升可读性与出版一致性。

## When to use / 何时使用

- "Apply our style guide to this draft."
- "按出版社风格统一这份文稿。"
- "Enforce punctuation and tone conventions."

## Inputs / 输入

- text: required
- style_guide: optional, house rules
- tone_target: optional, formal or neutral or lively
- strictness: optional, low or medium or high

## Output / 输出

- styled_text: style-normalized draft
- rule_hits: which style rules were applied
- exception_notes: where rules were intentionally not applied

## Boundaries / 边界

- Do not alter factual claims for style reasons.
- Preserve legal, quoted, or standardized wording when required.
- Mark rule conflicts explicitly.

## Execution Guidance / 执行指引

1. Parse style constraints and priorities.
2. Apply punctuation, tone, and format rules conservatively.
3. Record applied rules and exceptions.
4. Return revised text plus compact style report.

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
