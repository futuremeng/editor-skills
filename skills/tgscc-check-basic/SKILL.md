---
name: tgscc-check-basic
description: "Basic standard Chinese character compliance hints. / 基础通用规范汉字合规提示。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "字"
    requires: {}
---

# tgscc-check-basic

## Purpose / 目标

Provide a conservative character-level review for potentially non-standard Chinese forms.

对可能的非规范汉字形式进行保守型字符级提示。

## When to use / 何时使用

- "Check if this text has non-standard Chinese characters."
- "检查这段是否有不规范字。"
- "Need a quick traditional variant warning."

## Inputs / 输入

- text: required
- strict_mode: optional, true or false
- domain: optional, general or literature or historical

## Output / 输出

- findings: list of suspicious characters
- suggestions: candidate normalized forms
- confidence_notes: certainty and review advice

## Boundaries / 边界

- Do not force replacements for names or historical contexts.
- Mark domain-sensitive cases for human decision.
- Prefer warning over auto-normalization.

## Execution Guidance / 执行指引

1. Scan for uncommon or variant characters.
2. Suggest mainstream forms where confidence is reasonable.
3. Keep uncertain cases in a separate caution list.
4. Return compact actionable report.

## Prompt Contract / 提示约定

- Avoid over-correction.
- Preserve author style unless clearly non-standard.

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
