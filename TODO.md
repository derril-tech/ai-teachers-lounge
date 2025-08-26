# TODO — AI TEACHER'S LOUNGE
> [Code] deterministic systems • [Crew] agent‑generated content • [UI] frontend work

## Phase 0 — Repo & Infra
- [x] [Code] Monorepo scaffold: `apps/{frontend,gateway,orchestrator,workers}` + `packages/{sdk}`.
- [x] [Code] docker‑compose.dev: Postgres, Redis, NATS, MinIO (S3 API).
- [ ] [Code] CI: lint/typecheck/test, Docker build, SBOM + cosign, preview deploys.

## Phase 1 — DB, Auth, RBAC
- [x] [Code] Prisma/SQL migrations for full schema (units, lessons, sections, quizzes/items, activities/safety, inserts, UDL flags, approvals, exports, audit, snippets).
- [x] [Code] Auth.js + role mapping; RLS policies; Idempotency middleware.

## Phase 2 — Intake → Objectives/Sequence
- [x] [UI] BriefWizard (topic, grade band, period length, days, class size, equipment, inclusion notes).
- [x] [Crew] `objective-writer` (objectives + success criteria).
- [x] [Code] `sequence-planner` (time allocator, transitions, at least one formative check).
- [x] [UI] ObjectiveEditor, TimeBudgetGauge, SectionBuilder, FormativeCheckList.

## Phase 3 — Quiz Builder & Gradebook
- [x] [Crew] `quiz-builder` (item stems, distractors, answer keys, difficulty tiers).
- [x] [UI] QuizTable, RubricEditor, Gradebook (quick entry), CSV export.
- [x] [Code] Item validator (MCQ ≥3 choices, numeric tolerance, rubrics 1–4).

## Phase 4 — Activity Designer & Safety
- [x] [Crew] `activity-designer` + `science-lab` (steps, roles, materials, safety, cleanup).
- [x] [UI] ActivityDesigner, MaterialsList, SafetyChecklist (block export until completed).

## Phase 5 — Cross‑Discipline Inserts
- [x] [Crew] `timeline-historian`, `math-setter`, `science-lab` (slides, datasets/problems, lab sheet).
- [x] [UI] HistorySlides (MDX preview), MathProblemSet (dataset, core/challenge), ScienceLabSheet.

## Phase 6 — UDL Checker & Approvals
- [x] [Crew] `udl-checker` (flags & rewrites; reading level).
- [x] [UI] UDLPanel (apply rewrite), ApprovalsPanel (Coach → Lead chain), lock after approval.

## Phase 7 — Exports
- [x] [Crew] `reporter` (Pack PDF, Slides PDF/MDX, Worksheets PDF/DOCX, Quiz PDF), `exporter` (CSV grades, Bundle ZIP).
- [x] [Code] Signed URLs, change log, artifact versioning, export progress WS.

## Testing
- [x] **Unit**: time allocator, item validator, rubric scoring, UDL rules, safety gate.
- [x] **Contract**: OpenAPI + Zod schema round‑trips.
- [x] **E2E (Playwright)**: intake→objectives→sequence→quiz/activity→inserts→UDL→approvals→export.
- [x] **Load**: k6 parallel lesson generations & exports.
- [x] **Chaos**: zero‑equipment path, long periods, invalid item specs, missing materials.
- [x] **Security**: ZAP baseline, dependency & secret scans.

## Seeds & Demos
- [x] Seed unit "Renewable Energy (Grade 6)" with 2 lessons.
- [x] Sample datasets (kWh costs, capacity factors), 10 sample item templates per type.
- [x] Reusable safety snippets (heat/cutting/chemical‑free) in `snippets`.

## Runbooks
- [x] **Time budget overrun** → auto‑rebalance across sections; suggest split to 2‑day lesson.
- [x] **Safety incomplete** → block export; highlight missing PPE/heat/cleanup items.
- [x] **Low UDL coverage** → apply suggested rewrites; add visuals/sentence frames.
- [x] **Weak item bank** → increase generator count; filter by difficulty blueprint.

