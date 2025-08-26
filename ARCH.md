# Architecture — AI TEACHER’S LOUNGE

## Topology
- **Frontend**: Next.js 14 App Router (TS), shadcn/ui + Tailwind; TipTap editor (track changes); Recharts; TanStack Query + Zustand; WS client w/ SSE fallback; signed S3 URLs.
- **API Gateway**: NestJS REST /v1; OpenAPI 3.1; Zod/AJV validation; RBAC; rate limiting; Idempotency‑Key; Problem+JSON errors.
- **Auth**: Auth.js (OAuth/passwordless) + short‑lived JWT; SAML/OIDC; SCIM (districts).
- **Orchestrator**: CrewAI FastAPI w/ agents — History Teacher, Math Teacher, Science Teacher, Pedagogy Expert.
- **Workers (Python)**:
  - `intake-normalizer`, `objective-writer`, `sequence-planner`
  - `quiz-builder`, `activity-designer`, `science-lab`, `math-setter`, `timeline-historian`
  - `udl-checker`, `reporter`, `exporter`
- **Infra**: Postgres + pgvector; Redis; NATS; Celery; S3/R2; OTel + Prom/Grafana; Sentry; Secrets Manager/KMS.

## Data Model (highlights)
- **Tenancy/Roles**: `orgs`, `users`, `memberships` (`owner, admin, teacher, coach, lead, viewer`).
- **Units/Lessons**: `units`, `lessons` (status), `objectives`, `sections`, `vocab`, `misconceptions`.
- **Assessment**: `quizzes`, `items` (mcq/ms/numeric/short/label), `grades`.
- **Activities**: `activities` (steps, materials, safety, cleanup).
- **Inserts**: `hist_slides`, `math_sets` (dataset/core/challenge/solutions), `science_labs`.
- **UDL/Approvals/Exports/Audit**: `udl_flags`, `approvals`, `exports`, `comments`, `audit_log`.
- **Reuse Library**: `snippets` (pgvector embeddings).

## API Surface (REST /v1)
- **Auth/Me**: `/auth/login|refresh`, `/me`
- **Units/Lessons**: `/units`, `/units/:id/lessons`, `/lessons/:id`
- **Design**: `/lessons/:id/objectives`, `/sequence`, `/vocab`, `/misconceptions`, `/activity`, `/quiz`
- **Inserts**: `/lessons/:id/history`, `/math`, `/science`
- **UDL**: `/lessons/:id/udl/check`
- **Collab/Approvals**: `/comments`, `/lessons/:id/approvals`, `/lessons/:id/approve`
- **Grades/Exports**: `/grades/bulk`, `/lessons/:id/export`, `/exports/:id`

## Agent Tool Interfaces (strict)
- `Lesson.objectives(brief) → objectives[], success_criteria[]`
- `Lesson.sequence(objectives, constraints) → minutes[], sections[], transitions[], materials`
- `Lesson.vocab(topic, grade) → terms[], kid_friendly_defs[]`
- `Assessment.quiz(spec) → items[], answer_key, rubrics?`
- `Activity.design(kind, constraints) → steps[], materials[], safety[], roles[], cleanup[]`
- `History.timeline(topic, grade) → slides[], prompts[]`
- `Math.problems(dataset_spec) → dataset, core_set[], challenge_set[], solutions[]`
- `Science.lab(phenomenon, equipment) → lab_sheet, demo_steps, misconceptions[], checks[]`
- `UDL.check(lesson_pack) → flags[], rewrites[], reading_level`
- `Report.render(lessonId, targets[])` / `Export.bundle(lessonId, targets[])`

## Realtime Channels (WS)
- `lesson:{id}:drafts` (sections/items/inserts),
- `lesson:{id}:udl` (flags/rewrites),
- `lesson:{id}:approvals`,
- `export:{id}:status`.
Presence indicators; soft locks per section to avoid collisions.

## Guardrails
- **Approval disabled** if total minutes ≠ period_minutes × days or if no formative check present.
- **Activity required** safety checklist; export blocked until present.
- **Quiz export disabled** when any item lacks answer/points or fails validator.
- **No sensitive personal data**: grades use pseudonymous `student.alias`.

## Security & Privacy
- Postgres **RLS** per org; signed URLs (short‑lived) for exports; TLS 1.2+; AES‑256 at rest; KMS‑wrapped secrets.
- FERPA/COPPA/GDPR‑K aware: no student PII by default; retention policies; DSR endpoints (admin).
- Immutable `audit_log` for content generations, edits, approvals, exports.

## Deployment & SLOs
- FE: Vercel; APIs/Workers: Render/Fly or GKE pools (CPU for generation; mem‑opt for exports).
- Cache: Redis; Bus: NATS; Object Store: S3/R2; DB: Managed Postgres + pgvector; PITR.
- **SLOs (single‑day lesson)**: objectives+sequence < **3s**; quiz (10–12) < **4s**; activity < **3s**; UDL < **2.5s**; export < **10s**; WS P95 < **250ms**; 5xx < **0.5%/1k**.

