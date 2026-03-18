---
name: split-by-title-context
description: "Split long text by headings and local context windows. / 按标题和上下文窗口切分长文。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🧱"
    requires: {}
---

# split-by-title-context

## Purpose / 目标

Design a heading-aware segmentation result so each chunk remains semantically coherent for proofreading.

设计基于标题层级的切分方案，尽量保证每个分块语义完整，便于校对。

## When to use / 何时使用

- "Split this long article before proofreading."
- "先把这本书按章节切块。"
- "Need context-preserving chunks for LLM review."

## Inputs / 输入

- text: required, source content
- max_chunk_chars: optional, default 1500 to 2500
- min_chunk_chars: optional, default 500
- heading_levels: optional, for example H1-H3

## Output / 输出

- chunk_plan: ordered chunk definitions
- context_links: previous and next context hints
- edge_cases: sections that need manual review

## Boundaries / 边界

- Do not remove original content.
- Do not break inside code blocks, tables, or quotes when possible.
- Mark weak split points instead of forcing hard segmentation.

## Execution Guidance / 执行指引

1. Identify heading structure and section boundaries.
2. Build candidate chunks under max length.
3. Merge very short neighboring chunks.
4. Add context notes for each chunk.

## Prompt Contract / 提示约定

- Return a deterministic chunk index.
- Use explicit rationale for non-trivial merges.
- Surface uncertain boundaries.

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
