# editor-skills

Bilingual prompt-only skills for editing and proofreading workflows.

editor-skills 是一个中英双语、纯提示词（prompt-only）的技能仓库，面向编辑、校对、结构检查与差异分析场景。

## Repository Structure

- skills/: installable skills index path for CoPaw market
- templates/: reusable authoring templates

## Skill List

- proofread-single: single paragraph proofreading with minimal rewrites
- proofread-batch-plan: plan-only workflow for large batch proofreading
- split-by-title-context: split long text by heading and context windows
- sentence-split-zh: Chinese sentence segmentation and numbering
- sentence-align-diff: compare source and revised text with alignment notes
- tgscc-check-basic: basic check for standard Chinese character usage
- variant-word-suggest: suggest preferred variant word forms
- structure-title-number-check: verify heading levels and numbering continuity
- terminology-consistency-check: enforce cross-section terminology consistency
- proofreading-report-merge: merge chunk-level results into one final report
- chapter-quality-gate: evaluate sign-off readiness with quality gates
- change-risk-review: identify meaning drift and factual regression risks
- bilingual-consistency-check: verify Chinese-English semantic and term alignment
- numeric-unit-consistency: normalize numeric and unit writing consistency
- named-entity-consistency: keep person/place/org/product names stable
- citation-reference-check: validate citation and bibliography linkage integrity
- timeline-fact-consistency: detect chronology and cross-section fact conflicts
- release-readiness-check: provide final go or no-go before publication
- proofreading-decision-log: generate auditable rationale for editing decisions
- review-handoff-packager: package review outcomes for editor-author handoff
- proofread-style-enforcer: enforce style-guide rules with minimal meaning drift
- policy-sensitive-review: flag compliance-sensitive statements for human review

## Install with CoPaw

Option A: direct install from Git URL

copaw skills install git+https://github.com/futuremeng/editor-skills?index_path=skills

Option B: add market source into config

{
  "skills_market": {
    "markets": [
      {
        "url": "https://github.com/futuremeng/editor-skills",
        "index_path": "skills",
        "enabled": true,
        "order": 200
      }
    ]
  }
}

## Authoring Rules

- Directory name must match frontmatter name.
- Each skill directory must contain SKILL.md.
- Keep skills prompt-only for current phase. No executable scripts.
- Keep output schema explicit and stable.
- Bilingual sections should stay aligned semantically.

## Governance

- See CONTRIBUTING.md for contribution workflow.
- See CHANGELOG.md for release history.
- See skills/INDEX.md for current index inventory.
- See docs/skills-catalog.md for workflow-oriented skill navigation.
- See docs/skills-matrix.md for metadata and section coverage matrix.

## Quality Checks

Run local lint before opening a PR:

python3 scripts/lint_skills.py

Strict mode (warnings treated as failures):

python3 scripts/lint_skills.py --strict-warnings

JSON output for CI parsing:

python3 scripts/lint_skills.py --json

Regenerate skills matrix:

python3 scripts/generate_skills_matrix.py

## License

MIT
