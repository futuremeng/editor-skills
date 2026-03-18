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
