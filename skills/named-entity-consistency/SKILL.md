---
name: named-entity-consistency
description: "Ensure consistent naming for people, places, organizations, and products. / 保持人名地名机构名产品名一致。"
metadata:
  builtin_skill_version: "0.1.0"
  copaw:
    emoji: "🏷️"
    requires: {}
---

# named-entity-consistency

## Purpose / 目标

Track named entities across sections and detect alias drift, spelling variance, and inconsistent references.

追踪跨章节专有名词，识别别名漂移、拼写差异和引用不一致。

## When to use / 何时使用

- "Check named entities across chapters."
- "帮我统一人名地名机构名。"
- "Find inconsistent product names in this draft."

## Inputs / 输入

- text_or_sections: required
- canonical_list: optional, approved names
- transliteration_policy: optional, for cross-language names

## Output / 输出

- entity_map: canonical form and observed variants
- inconsistency_cases: where naming diverges
- resolution_actions: conservative normalization suggestions

## Boundaries / 边界

- Preserve quoted historical or legal names when necessary.
- Do not collapse distinct entities with similar names.
- Mark uncertain alias links as review-required.

## Execution Guidance / 执行指引

1. Extract named entities by context.
2. Build canonical-to-variant mapping.
3. Identify inconsistent references.
4. Output fixes and exceptions with traceability.
