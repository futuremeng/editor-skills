---
name: bilingual-consistency-check
description: "Check cross-language consistency between Chinese and English content. / 检查中英双语内容的一致性。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🌐"
    requires: {}
---

# bilingual-consistency-check

## Purpose / 目标

Review bilingual text pairs and identify inconsistencies in meaning, terminology, numbers, and named entities.

核查双语文本对在语义、术语、数字和专有名词上的一致性。

## When to use / 何时使用

- "Check Chinese and English consistency for this section."
- "帮我检查中英文对照是否一致。"
- "Find mismatch between source and translation."

## Inputs / 输入

- zh_text: required, Chinese content
- en_text: required, English content
- domain_terms: optional, glossary or term list
- strictness: optional, low or medium or high

## Output / 输出

- mismatch_list: issue list by type (meaning, term, number, entity)
- correction_suggestions: conservative bilingual revision hints
- unresolved_items: items requiring human decision

## Boundaries / 边界

- Do not rewrite both sides aggressively.
- Do not assume cultural adaptation unless requested.
- Keep uncertain semantic gaps explicitly flagged.

## Execution Guidance / 执行指引

1. Align bilingual units by paragraph or sentence.
2. Compare semantic intent and factual details.
3. Check terms, numbers, dates, and names.
4. Output mismatches with concise fix proposals.

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

## Prompt Contract / 提示约定

- Keep recommendations conservative and traceable.
- Separate confirmed findings from uncertain assumptions.
- Preserve original intent unless explicit rewrite is requested.
- If confidence is low, provide options and mark review-required items.
