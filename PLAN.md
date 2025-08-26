# Project Plan — AI TEACHER’S LOUNGE

> Scope: A multi‑agent lesson design studio that converts a brief like “Teach middle schoolers about renewable energy.” into a complete lesson pack: objectives & success criteria, timed sequence, quiz bank (auto/teacher‑graded), hands‑on activities w/ safety, cross‑discipline inserts (History/Math/Science), UDL/differentiation, teacher notes, family letter, and exportable slides/worksheets/gradebook.

## Product Goal
Deliver a **teacher‑first planning cockpit** that reduces lesson design time while **raising classroom practicality** (timing fit, safety, UDL). Outputs must be **print‑ready**, classroom‑safe, and easily reviewed by coaches/leads.

## Safety & Scope
- Planning **simulation/templates**; not a replacement for district policies or local curriculum governance.
- No medical/psychological/personal advice to students; hands‑on tasks include **non‑hazardous** materials and explicit **safety checklists**.
- Student data is **pseudonymous by default**; no DOB/emails/addresses required.

## 80/20 Build Strategy
- **80% deterministic**: timing allocator, sequence validator, quiz schema, rubric & grade CSVs, export pipeline, approvals, UDL checks, safety gates.
- **20% agents**: objective phrasing, kid‑friendly vocabulary, activity & materials drafts, cross‑discipline inserts, item stem/distractor generation, tone harmonization.

## Immediate Next 3 Tasks
1. **Monorepo scaffold & infra** (`apps/{web,gateway,orchestrator,workers}`) with docker‑compose (Postgres + Redis + MinIO/S3 + NATS).
2. **DB migrations** for units/lessons, sections, quizzes/items, activities/safety, inserts (hist/math/sci), UDL flags, approvals, exports, audit.
3. **Lesson intake to first draft**: brief → objectives+success criteria → timed sequence with at least one formative check.

## Phases
- **P0** Infra, CI, auth/RBAC
- **P1** Lesson intake → objectives/sequence/vocab/misconceptions
- **P2** Quiz builder (10–12 items), rubrics, gradebook CSV
- **P3** Activity designer (lab/build/discussion) + safety checklist
- **P4** Cross‑discipline inserts (History/Math/Science)
- **P5** UDL checker + rewrites; approvals
- **P6** Exports (Pack PDF, Slides PDF/MDX, Worksheets PDF/DOCX, Quiz PDF/CSV, Bundle)
- **P7** Observability, polishing, samples

## MVP Definition of Done
- Single‑day lesson (45–60 min) with **time‑balanced sequence** (≤ ±2 min).
- ≥ 8 quiz items across types with answer keys; ≥ 1 rubric.
- One hands‑on **activity** with materials list and **safety** notes.
- Cross‑discipline inserts present (at least two of three).
- UDL flags ≤ 2 low‑severity; at least one scaffold applied.
- Coach→Lead approval gates; export bundle delivers **Pack PDF, Slides PDF, Worksheets PDF, Quiz PDF, CSV Gradebook, JSON**.

## Risks & Mitigations
- **Time budget drift** → live gauge + auto‑rebalance and section time caps.
- **Activity safety gaps** → mandatory safety checklist & blocked export until filled.
- **Item quality variance** → item validator (choices ≥3, plausible distractors), difficulty tags.
- **Reading level mismatch** → Pedagogy agent “simplify to grade band” rewrite with preview diff.

## KPIs
- **Time‑to‑teachable** ≤ 15 min median from intake to approved pack.
- **UDL coverage**: ≥ 80% lessons pass with ≤ 2 low‑severity flags.
- **Assessment readiness**: ≥ 10 well‑formed items per lesson on average.
- **Export reliability** ≥ 99% successful deliveries.

