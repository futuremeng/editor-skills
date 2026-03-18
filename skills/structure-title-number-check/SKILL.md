---
name: structure-title-number-check
description: "Check heading hierarchy and numbering continuity. / 检查标题层级与编号连续性。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🧭"
    requires: {}
---

# structure-title-number-check

## Purpose / 目标

Validate document structural consistency, including heading levels and numbering sequences.

校验文档结构一致性，包括标题层级和编号序列连续性。

## When to use / 何时使用

- "Check structure issues in this chapter."
- "帮我检查标题层级和编号是否连续。"
- "Find missing or duplicated section numbers."

## Inputs / 输入

- text: required
- heading_style: optional, markdown or custom
- numbering_scheme: optional, arabic or chinese or mixed

## Output / 输出

- structure_findings: hierarchy and numbering issues
- suggested_fixes: minimal correction proposals
- risk_zones: sections requiring manual confirmation

## Boundaries / 边界

- Do not reorder content automatically.
- Do not assume one numbering standard without input.
- Flag ambiguous structures instead of forcing a rule.

## Execution Guidance / 执行指引

1. Parse heading and numbering tokens.
2. Build a logical outline tree.
3. Detect jumps, duplicates, or resets.
4. Return issue list with minimal fix suggestions.

## Prompt Contract / 提示约定

- Provide issue location hints by nearest heading text.
- Keep fix suggestions conservative.
