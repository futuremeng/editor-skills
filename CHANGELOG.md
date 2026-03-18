# Changelog

## 0.5.1 - 2026-03-18

- Add `## Prompt Contract / 提示约定` to 14 skills that previously emitted lint warnings.
- `python3 scripts/lint_skills.py --strict-warnings` now passes for all 22 skills.

## 0.5.0 - 2026-03-18

- Upgrade `scripts/lint_skills.py` with:
  - severity levels (`error` / `warn`)
  - JSON output (`--json`)
  - strict warning gate (`--strict-warnings`)
- Add `scripts/generate_skills_matrix.py` to auto-generate skills matrix docs.
- Add generated docs page: `docs/skills-matrix.md`.
- Update README and CONTRIBUTING with new quality workflow commands.

## 0.4.0 - 2026-03-18

- Add `Example I/O / 示例输入输出` section to all 22 skills.
- Add `scripts/lint_skills.py` for frontmatter and section validation.
- Add `docs/skills-catalog.md` for workflow-oriented skill discovery.
- Update README and CONTRIBUTING with quality check guidance.

## 0.3.0 - 2026-03-18

- Add 4 collaboration and governance skills:
  - proofreading-decision-log
  - review-handoff-packager
  - proofread-style-enforcer
  - policy-sensitive-review
- Expand total skill count from 18 to 22.

## 0.2.0 - 2026-03-18

- Add 6 advanced consistency and release-gate skills:
  - bilingual-consistency-check
  - numeric-unit-consistency
  - named-entity-consistency
  - citation-reference-check
  - timeline-fact-consistency
  - release-readiness-check
- Expand total skill count from 12 to 18.

## 0.1.0 - 2026-03-18

- Initialize repository structure for skills market indexing.
- Add bilingual prompt-only skill template.
- Add 12 MVP and Phase-2 baseline skills:
  - proofread-single
  - proofread-batch-plan
  - split-by-title-context
  - sentence-split-zh
  - sentence-align-diff
  - tgscc-check-basic
  - variant-word-suggest
  - structure-title-number-check
  - terminology-consistency-check
  - proofreading-report-merge
  - chapter-quality-gate
  - change-risk-review
- Add contributing guide and repository license.
