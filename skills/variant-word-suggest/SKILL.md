---
name: variant-word-suggest
description: "Suggest preferred forms for variant words. / 提供异形词的推荐词形。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "📚"
    requires: {}
---

# variant-word-suggest

## Purpose / 目标

Identify variant word forms and suggest a consistent preferred form for editorial quality.

识别异形词并给出一致的推荐词形，提升文稿规范性。

## When to use / 何时使用

- "Normalize variant words in this section."
- "这章里异形词要统一一下。"
- "Need term consistency before publication."

## Inputs / 输入

- text: required
- style_target: optional, modern or academic or publishing
- preserve_quote: optional, true or false

## Output / 输出

- normalization_list: source form and suggested form
- consistency_summary: repeated terms and chosen canonical form
- exceptions: terms intentionally kept

## Boundaries / 边界

- Do not rewrite quoted historical forms by default.
- Do not change specialized terms without explicit confidence.
- If multiple valid standards exist, present options.

## Execution Guidance / 执行指引

1. Extract candidate variant words.
2. Cluster same-meaning forms.
3. Propose canonical form based on target style.
4. Output replacements and exceptions.

## Prompt Contract / 提示约定

- Keep terminology decisions transparent.
- Prefer consistency and traceability.
