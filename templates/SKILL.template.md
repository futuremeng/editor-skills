---
name: your-skill-name
description: "One-line bilingual description / 一行双语描述"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🧩"
    requires: {}
---

# your-skill-name

## Purpose / 目标

Describe what this skill should do in one paragraph.

用一段话说明技能目标。

## When to use / 何时使用

- Trigger phrase 1
- Trigger phrase 2

## Inputs / 输入

- input_1: type, meaning
- input_2: type, meaning

## Output / 输出

- format: stable structure
- include: assumptions, uncertainties, next actions

## Boundaries / 边界

- What this skill must not do.
- How to handle missing information.

## Execution Guidance / 执行指引

1. Restate task in one sentence.
2. Extract constraints and priorities.
3. Produce output with explicit sections.
4. Add risk notes if confidence is low.

## Prompt Skeleton / 提示骨架

Role:
You are a domain-focused assistant for this skill.

Instructions:
- Keep edits minimal and preserve original intent.
- Explain trade-offs when multiple options exist.
- Use bilingual wording where useful.

Output Contract:
- Section 1: Result
- Section 2: Rationale
- Section 3: Follow-ups
