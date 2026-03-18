---
name: timeline-fact-consistency
description: "Check chronology and fact consistency across long-form text. / 检查长文中的时间线与事实一致性。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🕰️"
    requires: {}
---

# timeline-fact-consistency

## Purpose / 目标

Detect timeline contradictions and factual sequence conflicts in narrative or technical documents.

识别叙事或技术文档中的时间线冲突和事实顺序矛盾。

## When to use / 何时使用

- "Check chronology consistency in this manuscript."
- "帮我核对事件前后顺序是否一致。"
- "Find date and timeline conflicts across chapters."

## Inputs / 输入

- text_or_sections: required
- timeline_scope: optional, chapter or full-document
- fact_priority: optional, strict or balanced

## Output / 输出

- timeline_conflicts: contradictory dates or event orders
- fact_conflicts: inconsistent factual claims
- mitigation_plan: merge or rewrite suggestions

## Boundaries / 边界

- Do not infer unstated events as facts.
- Keep uncertain temporal relations flagged.
- Separate hard conflict from soft ambiguity.

## Execution Guidance / 执行指引

1. Extract events, dates, and temporal cues.
2. Build ordered timeline graph.
3. Detect sequence and fact conflicts.
4. Return evidence-based issue report.
