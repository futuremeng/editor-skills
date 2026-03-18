---
name: numeric-unit-consistency
description: "Validate number and unit consistency across a document. / 校验全文数字与单位一致性。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "📏"
    requires: {}
---

# numeric-unit-consistency

## Purpose / 目标

Detect inconsistent number formats, units, scales, and conversion expressions.

识别数字格式、单位写法、量纲尺度和换算表达的不一致问题。

## When to use / 何时使用

- "Check all numbers and units in this report."
- "请统一本文中的数字和单位格式。"
- "Find unit conversion errors."

## Inputs / 输入

- text: required
- unit_style: optional, SI or local or mixed
- decimal_policy: optional, precision rules
- locale: optional, zh-CN or en-US or custom

## Output / 输出

- findings: inconsistent number or unit cases
- normalization_plan: standardized writing recommendations
- high_risk_items: possible conversion or magnitude risks

## Boundaries / 边界

- Do not change scientific meaning without evidence.
- Keep original values unless clear formatting normalization is needed.
- Flag possible conversion errors instead of guessing corrected values.

## Execution Guidance / 执行指引

1. Extract numeric and unit tokens.
2. Group by metric concept and usage context.
3. Detect inconsistent styles and suspicious conversions.
4. Return prioritized fixes with examples.
