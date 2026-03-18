---
name: citation-reference-check
description: "Check citation and reference linkage consistency. / 检查引用与参考文献关联一致性。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🔗"
    requires: {}
---

# citation-reference-check

## Purpose / 目标

Validate in-text citations, footnotes, and reference entries for completeness and linkage correctness.

校验正文引用、脚注和参考文献条目的完整性与关联正确性。

## When to use / 何时使用

- "Check citation integrity in this paper."
- "帮我检查文内引用和参考文献是否对应。"
- "Find missing or duplicated references."

## Inputs / 输入

- text: required
- reference_style: optional, APA or MLA or GB/T or custom
- include_footnotes: optional, true or false

## Output / 输出

- citation_issues: missing, duplicated, malformed, orphaned
- linkage_report: in-text to reference mapping quality
- fix_suggestions: minimal corrective actions

## Boundaries / 边界

- Do not fabricate missing bibliographic details.
- Keep style recommendations aligned with requested standard.
- Mark ambiguous mappings for manual verification.

## Execution Guidance / 执行指引

1. Extract citation markers and reference entries.
2. Build mapping graph between markers and entries.
3. Detect missing, duplicate, and format anomalies.
4. Return issue list and correction checklist.

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
