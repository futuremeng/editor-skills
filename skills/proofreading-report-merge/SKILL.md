---
name: proofreading-report-merge
description: "Merge chunk-level proofreading notes into one final report. / 汇总分块校对结果为最终报告。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🧾"
    requires: {}
---

# proofreading-report-merge

## Purpose / 目标

Consolidate multi-chunk proofreading outcomes into a single, review-ready report.

把多分块校对结果合并为统一的可审阅报告。

## When to use / 何时使用

- "Merge all chapter proofreading notes."
- "把所有分段结果汇总成一份。"
- "Need one final report for editorial sign-off."

## Inputs / 输入

- chunk_reports: required, list of chapter or chunk notes
- output_style: optional, concise or detailed
- priority_rules: optional, severity-first or chapter-first

## Output / 输出

- executive_summary: top issues and global stats
- issue_catalog: deduplicated issue list
- action_items: prioritized fix checklist

## Boundaries / 边界

- Do not drop high-severity items during deduplication.
- Keep traceability to source chunk IDs.
- Mark conflicting recommendations explicitly.

## Execution Guidance / 执行指引

1. Normalize field names from each chunk report.
2. Merge and deduplicate by issue signature.
3. Sort by severity and impact.
4. Return summary plus actionable backlog.
