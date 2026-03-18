# Skills Matrix

Auto-generated inventory of skill metadata and section coverage.

自动生成的技能元数据与章节覆盖矩阵。

Total skills: 22

| Skill | Description | Section Coverage | Example I/O |
| --- | --- | --- | --- |
| bilingual-consistency-check | Check cross-language consistency between Chinese and English content. / 检查中英双语内容的一致性。 | 6/6 | yes |
| change-risk-review | Review revision risks such as meaning drift and factual regression. / 审查修订引入的语义漂移与事实回退风险。 | 6/6 | yes |
| chapter-quality-gate | Apply acceptance gates before chapter sign-off. / 章节签发前质量闸门检查。 | 6/6 | yes |
| citation-reference-check | Check citation and reference linkage consistency. / 检查引用与参考文献关联一致性。 | 6/6 | yes |
| named-entity-consistency | Ensure consistent naming for people, places, organizations, and products. / 保持人名地名机构名产品名一致。 | 6/6 | yes |
| numeric-unit-consistency | Validate number and unit consistency across a document. / 校验全文数字与单位一致性。 | 6/6 | yes |
| policy-sensitive-review | Flag policy and compliance sensitive expressions for human review. / 标注政策与合规敏感表达供人工复核。 | 6/6 | yes |
| proofread-batch-plan | Plan-only workflow for large proofreading tasks. / 大规模校对任务的规划型技能（不执行脚本）。 | 6/6 | yes |
| proofread-single | Proofread one paragraph with minimal meaning drift. / 单段精校，尽量不改变原意。 | 6/6 | yes |
| proofread-style-enforcer | Enforce writing style guide while preserving meaning. / 在保留原意前提下执行文风规范。 | 6/6 | yes |
| proofreading-decision-log | Generate auditable logs for proofreading decisions. / 生成可审计的校对决策日志。 | 6/6 | yes |
| proofreading-report-merge | Merge chunk-level proofreading notes into one final report. / 汇总分块校对结果为最终报告。 | 6/6 | yes |
| release-readiness-check | Run pre-release editorial quality gates. / 执行发布前编辑质量总闸门检查。 | 6/6 | yes |
| review-handoff-packager | Package proofreading outcomes for editor-author handoff. / 打包校对结果用于编辑与作者交接。 | 6/6 | yes |
| sentence-align-diff | Align source and revised sentences and summarize diffs. / 原文与修订文句级对齐并总结差异。 | 6/6 | yes |
| sentence-split-zh | Chinese sentence segmentation with stable numbering. / 中文句子切分与稳定编号。 | 6/6 | yes |
| split-by-title-context | Split long text by headings and local context windows. / 按标题和上下文窗口切分长文。 | 6/6 | yes |
| structure-title-number-check | Check heading hierarchy and numbering continuity. / 检查标题层级与编号连续性。 | 6/6 | yes |
| terminology-consistency-check | Check terminology consistency across sections. / 跨章节术语一致性检查。 | 6/6 | yes |
| tgscc-check-basic | Basic standard Chinese character compliance hints. / 基础通用规范汉字合规提示。 | 6/6 | yes |
| timeline-fact-consistency | Check chronology and fact consistency across long-form text. / 检查长文中的时间线与事实一致性。 | 6/6 | yes |
| variant-word-suggest | Suggest preferred forms for variant words. / 提供异形词的推荐词形。 | 6/6 | yes |

## Usage

Regenerate this file with:

python3 scripts/generate_skills_matrix.py
