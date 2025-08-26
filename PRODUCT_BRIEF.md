AI TEACHER’S LOUNGE — END‑TO‑END PRODUCT BLUEPRINT
(React 18 + Next.js 14 App Router; CrewAI multi‑agent orchestration; TypeScript‑first contracts.)
1) Product Description & Presentation
One‑liner
A multi‑agent lesson design studio where History Teacher, Math Teacher, Science Teacher, and Pedagogy Expert transform a brief like “Teach middle schoolers about renewable energy.” into a complete lesson pack: day plan(s) with timing & standards tags, quiz (auto‑/teacher‑graded), hands‑on activities with materials & safety, differentiation & scaffolds, teacher notes, family letter, and exportable slides/worksheets.
What it produces
•
Lesson plan (objectives, success criteria, timing, vocabulary, misconceptions, UDL/differentiation, formative checks).
•
Cross‑discipline inserts
o
Science: principles (energy conversion, wind/solar, efficiency).
o
Math: proportional reasoning, kWh cost calc, graph reading.
o
History: timeline of energy transitions, policy inflection points.
•
Assessment: quiz bank (MCQ, multi‑select, numeric, short answer, labeling), answer keys, rubrics, auto‑grading rules.
•
Activities: inquiry lab + build (e.g., mini solar oven), group roles, materials, safety checklist, cleanup, extensions.
•
Teacher kit: projector script, discussion prompts, exit ticket, family letter, optional homework.
•
Exports: PDF Lesson Pack, PDF/MDX Slides, DOCX/PDF Worksheets, CSV Gradebook, JSON Bundle.
Scope/Safety
•
Classroom planning simulation. Not a replacement for local curriculum governance. Content avoids personal advice; safety checklists for hands‑on tasks.
2) Target User
•
Middle‑school teachers (Science/Math/History) & instructional coaches.
•
Curriculum leads building units.
•
Ed‑tech vendors & NGOs prototyping lesson kits.
•
Teacher prep programs practicing lesson design.
3) Features & Functionalities (Extensive)
Intake & Constraints
•
Brief wizard: topic, grade band (5–8), period length, number of days, class size, equipment availability (hot glue, thermometers, multimeters), room type (lab/classroom), reading level target, assessment preference, inclusion notes (ELL/IEP/504), local priorities (sustainability week, school policies).
•
Standards tags: user‑selectable tags (science practices, math practices, history themes).
•
Content policy toggles: avoid politics; avoid commercial brands; safe‑tools list.
Lesson Design
•
Objective builder: measurable objectives + success criteria; Bloom/Cognitive level tags.
•
Sequence: Do‑Now → Concept Launch → Mini‑lesson → Guided Practice → Lab/Activity → Share‑out → Exit Ticket.
•
Timing engine: auto‑allocates minutes; respects period length & transitions.
•
Vocabulary & Misconceptions list (kid‑friendly).
•
Differentiation: ELL supports (sentence frames, visuals), IEP accommodations (chunking, extended time), extension challenges, alternate pathways when equipment limited.
•
Formative checks: cold‑call prompts, turn‑and‑talk stems, mini‑whiteboard checks.
Assessment & Materials
•
Quiz generator: item types, randomization, difficulty tiers, rationale text; conversion to PDF/Google‑form‑like MDX.
•
Rubrics for open responses (1–4 scale with descriptors).
•
Grade capture: quick mark entry & CSV export.
•
Materials & safety: consumables non‑hazardous list, PPE reminders, heat cautions, cleanup steps, disposal notes.
Multi‑Discipline Weaving
•
History Teacher adds 6–10 slide mini‑timeline + primary‑source prompt.
•
Math Teacher adds dataset (cost of energy, capacity factors) + two problem sets (core & challenge).
•
Science Teacher adds demo(s) and conceptual questions, plus lab sheet.
•
Pedagogy Expert harmonizes tone and age level; enforces UDL & checks bias/sensitivity.
Collaboration & Governance
•
Roles: Teacher, Curriculum Lead, Coach, Viewer.
•
Comment threads, suggestions, redlines with accept/reject; versioning & diffs.
•
Approval gates: Coach → Lead → Publish.
•
Collections: units composed of lessons; copy/branch for sections.
Exports
•
Lesson Pack PDF, Slides (MDX→PDF), Worksheets (PDF/DOCX), Quiz (PDF/CSV), Gradebook CSV, Family Letter (PDF), JSON Bundle (replayable).
4) Backend Architecture (Extremely Detailed & Deployment‑Ready)
4.1 Topology
•
Frontend/BFF: Next.js 14 (Vercel). Server Actions for light mutations & signed S3 URLs; SSR for read views.
•
API Gateway: Node/NestJS
o
REST /v1, OpenAPI 3.1; Zod/AJV validation; RBAC, rate limits, Idempotency‑Key, Problem+JSON.
•
Auth: Auth.js (OAuth/passwordless) with short‑lived JWT (rotating refresh); SAML/OIDC for districts; SCIM for org provisioning.
•
Orchestration: CrewAI Orchestrator (Python FastAPI) coordinating:
o
History Teacher (context & timeline, sources prompts, civics cautions)
o
Math Teacher (problems, datasets, graphing prompts, answer keys)
o
Science Teacher (concept framing, demos, labs, safety)
o
Pedagogy Expert (UDL, scaffolds, readability, behavior management prompts)
•
Workers (Python):
o
intake-normalizer (brief → structured constraints)
o
objective-writer (objectives & success criteria from topic/grade)
o
sequence-planner (minute‑by‑minute outline)
o
quiz-builder (items, keys, distractors, rubrics)
o
activity-designer (materials, steps, safety, group roles)
o
timeline-historian (history mini‑lesson & prompts)
o
math-setter (datasets & problem sets with solutions)
o
science-lab (lab sheet & demo steps)
o
udl-checker (scaffold assessment; reading level adjuster)
o
reporter (PDF/MDX/DOCX pack)
o
exporter (CSV/ZIP bundle)
•
Event Bus: NATS (lesson.*, quiz.*, activity.*, timeline.*, math.*, science.*, udl.*, export.*).
•
Task Queue: Celery (NATS/Redis backend) with lanes interactive (drafting), models (pack build), exports.
•
DB: Postgres (Neon/Cloud SQL) + pgvector (reusable snippets, exemplar items).
•
Object Storage: S3/R2 (exports, slide images, worksheet PDFs).
•
Cache: Upstash Redis (active lesson state, draft artifacts).
•
Realtime: WebSocket gateway (NestJS) + SSE fallback (draft streams, review gates, export progress).
•
Observability: OpenTelemetry traces; Prometheus/Grafana; Sentry; structured logs.
•
Secrets: Cloud Secrets Manager/Vault; KMS‑wrapped; no plaintext secrets.
4.2 CrewAI Agents & Tool Interfaces
Agents
•
History Teacher — 10‑slide context, primary‑source prompt, caution on presentism.
•
Math Teacher — numeric tasks (rates, unit conversions, graph read/write), scaffolds, answer keys.
•
Science Teacher — concept explanation, inquiry questions, lab sheet with variables & controls, safety.
•
Pedagogy Expert — timing, UDL, differentiation, sentence frames, discussion norms, formative checks; consistency.
Tool Interfaces (strict)
•
Lesson.objectives(brief) → {objectives[], success_criteria[]}
•
Lesson.sequence(objectives, constraints) → {minutes[], sections[], transitions[], materials}
•
Lesson.vocab(topic, grade) → {terms[], kid_friendly_defs[]}
•
Assessment.quiz(spec) → {items[], answer_key, rubrics?}
•
Activity.design(kind, constraints) → {steps[], materials[], safety[], roles[], cleanup[]}
•
History.timeline(topic, grade) → {slides[], prompts[]} (generic, no external citations injected)
•
Math.problems(dataset_spec) → {dataset, core_set[], challenge_set[], solutions[]}
•
Science.lab(phenomenon, equipment) → {lab_sheet, demo_steps, misconceptions[], checks[]}
•
UDL.check(lesson_pack) → {flags[], rewrites[], reading_level}
•
Report.render(lessonId, targets[]) / Export.bundle(lessonId, targets[])
4.3 Data Model (Postgres + pgvector)
-- Tenancy & Identity CREATE TABLE orgs ( id UUID PRIMARY KEY, name TEXT NOT NULL, plan TEXT, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE users ( id UUID PRIMARY KEY, org_id UUID REFERENCES orgs(id), email CITEXT UNIQUE, name TEXT, role TEXT, tz TEXT, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE memberships ( user_id UUID REFERENCES users(id), org_id UUID REFERENCES orgs(id), workspace_role TEXT CHECK (workspace_role IN ('owner','admin','teacher','coach','lead','viewer')), PRIMARY KEY (user_id, org_id) ); -- Classes & Rosters (pseudonymous by default) CREATE TABLE classes ( id UUID PRIMARY KEY, org_id UUID, name TEXT, grade_band TEXT, period_minutes INT, created_by UUID, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE students ( id UUID PRIMARY KEY, class_id UUID REFERENCES classes(id), alias TEXT, -- e.g., "S1", "learner-17" (no PII by default) notes TEXT ); -- Lessons & Units CREATE TABLE units ( id UUID PRIMARY KEY, org_id UUID, title TEXT, description TEXT, tags TEXT[], created_by UUID, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE lessons ( id UUID PRIMARY KEY, unit_id UUID REFERENCES units(id), title TEXT, topic TEXT, grade_band TEXT, period_minutes INT, days
INT DEFAULT 1, status TEXT CHECK (status IN ('created','drafting','review','approved','exported','archived')) DEFAULT 'created', created_by UUID, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE objectives ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), text TEXT, success_criteria TEXT ); CREATE TABLE sections ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), order_idx INT, name TEXT, minutes INT, content_md TEXT, materials JSONB, formative_check TEXT ); CREATE TABLE vocab ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), term TEXT, kid_def TEXT ); CREATE TABLE misconceptions ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), text TEXT, correction TEXT ); -- Assessments CREATE TABLE quizzes ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), title TEXT, total_points INT, randomize BOOLEAN DEFAULT TRUE ); CREATE TABLE items ( id UUID PRIMARY KEY, quiz_id UUID REFERENCES quizzes(id), type TEXT, -- 'mcq','ms','numeric','short','label' stem TEXT, choices JSONB, answer JSONB, rubric JSONB, points INT ); CREATE TABLE grades ( id UUID PRIMARY KEY, quiz_id UUID, student_id UUID, item_id UUID, score NUMERIC, feedback TEXT );
-- Activities & Safety CREATE TABLE activities ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), kind TEXT, -- 'lab','build','simulation','discussion' steps_md TEXT, group_roles JSONB, materials JSONB, safety JSONB, cleanup JSONB ); -- Cross-discipline Inserts CREATE TABLE hist_slides ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), slide_order INT, mdx TEXT, prompt TEXT ); CREATE TABLE math_sets ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), dataset JSONB, core JSONB, challenge JSONB, solutions JSONB ); CREATE TABLE science_labs ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), lab_sheet_md TEXT, demo_steps_md TEXT ); -- UDL & Reviews CREATE TABLE udl_flags ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), severity TEXT, message TEXT, rewrite TEXT ); CREATE TABLE approvals ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), order_idx INT, role_required TEXT, user_id UUID, status TEXT CHECK (status IN ('pending','approved','rejected')) DEFAULT 'pending', comment TEXT, acted_at TIMESTAMPTZ ); -- Exports & Audit CREATE TABLE exports ( id UUID PRIMARY KEY, lesson_id UUID REFERENCES lessons(id), kind TEXT, s3_key TEXT, meta JSONB, created_at TIMESTAMPTZ DEFAULT
now() ); CREATE TABLE comments ( id UUID PRIMARY KEY, lesson_id UUID, author_id UUID, anchor JSONB, body TEXT, created_at TIMESTAMPTZ DEFAULT now() ); CREATE TABLE audit_log ( id BIGSERIAL PRIMARY KEY, org_id UUID, user_id UUID, lesson_id UUID, action TEXT, target TEXT, meta JSONB, created_at TIMESTAMPTZ DEFAULT now() ); -- Reuse Library (embeddings) CREATE TABLE snippets ( id UUID PRIMARY KEY, org_id UUID, kind TEXT, content TEXT, tags TEXT[], embedding VECTOR(1536) );
Indexes & Constraints
•
CREATE INDEX ON sections (lesson_id, order_idx);
•
CHECK (sum(minutes) over lesson == period_minutes*days) enforced in API before approval.
•
Vector index on snippets.embedding.
•
Service invariants: cannot move lesson to approved without ≥1 formative check and ≥1 safety note if an activity is present.
4.4 API Surface (REST /v1, OpenAPI)
Auth & Orgs
•
POST /v1/auth/login / POST /v1/auth/refresh / GET /v1/me
Units & Lessons
•
POST /v1/units {title,description,tags}
•
POST /v1/units/:id/lessons {title,topic,grade_band,period_minutes,days}
•
GET /v1/lessons/:id snapshot
Design & Content
•
POST /v1/lessons/:id/objectives {fromBrief:true|false, upserts:[...]}
•
POST /v1/lessons/:id/sequence {constraints,...} → sections with minutes & materials
•
POST /v1/lessons/:id/vocab {terms?}
•
POST /v1/lessons/:id/misconceptions {upserts:[...]}
•
POST /v1/lessons/:id/activity {kind, constraints}
•
POST /v1/lessons/:id/quiz {spec} → items & key
•
POST /v1/lessons/:id/history / math / science (insert generators)
•
POST /v1/lessons/:id/udl/check → flags & rewrites
Collab & Approvals
•
POST /v1/comments {lesson_id, anchor, body}
•
POST /v1/lessons/:id/approvals {chain:[{order_idx,role_required}]}
•
POST /v1/lessons/:id/approve {order_idx, decision, comment}
Grades & Exports
•
POST /v1/grades/bulk {quiz_id, scores:[{student_alias,item_id,score,feedback?}]}
•
POST /v1/lessons/:id/export {targets:['pack_pdf','slides_pdf','worksheets_pdf','quiz_pdf','csv_grades','bundle_zip']}
•
GET /v1/exports/:id → signed URL
Conventions
•
Mutations require Idempotency‑Key.
•
Errors as Problem+JSON with remediation.
•
RLS by org; class scoping for grades.
4.5 Orchestration Logic (CrewAI)
State machine
created → drafting (objectives/sequence) → inserts (hist/math/sci) → assessment/activity → udl review → approvals → approved → exported → archived
Turn sequence
1.
intake-normalizer → constraints; objective-writer creates objectives & criteria.
2.
sequence-planner assigns sections & minutes; lesson.vocab & misconceptions.
3.
History/Math/Science insert generators create their sections.
4.
activity-designer & quiz-builder generate activity + quiz; science-lab adds lab sheet; math-setter adds datasets & keys.
5.
udl-checker flags reading level & scaffolds; rewrites applied.
6.
Approvals chain passes → reporter/exporter build artifacts.
4.6 Background Jobs
•
BuildObjectives(lessonId)
•
PlanSequence(lessonId)
•
GenerateQuiz(lessonId)
•
DesignActivity(lessonId)
•
InsertHistory/Math/Science(lessonId)
•
RunUDLCheck(lessonId)
•
ExportBundle(lessonId, targets[])
•
Periodics: SnippetHarvest, RetentionSweep, AlertOnFailure.
4.7 Realtime
•
WS channels:
o
lesson:{id}:drafts (sections, inserts, quiz)
o
lesson:{id}:udl (flags/rewrites)
o
lesson:{id}:approvals (gate status)
o
export:{id}:status
•
Presence: show co‑editors; soft locks per section to avoid collisions.
4.8 Caching & Performance
•
Redis caches: current sections, quiz items, inserts, last UDL pass, export manifests.
•
SLOs (single‑day lesson):
o
Objectives+sequence < 3 s P95.
o
Quiz (10–12 items) < 4 s P95.
o
Activity design < 3 s P95.
o
Full pack export < 10 s P95.
o
WS event delivery < 250 ms P95.
4.9 Observability
•
OTel spans with tags: lesson_id, phase, tokens/cost.
•
Metrics: time‑to‑first draft, UDL flags per lesson, approval pass rate, export success.
•
Logs: structured JSON; audit_log on edits, approvals, exports.
5) Frontend Architecture (React 18 + Next.js 14)
5.1 Tech Choices
•
Next.js 14 App Router, TypeScript.
•
UI: shadcn/ui + Tailwind (calm “planning dashboard” aesthetic).
•
Editors: TipTap (rich text/MDX with suggestions/track changes).
•
Charts: Recharts (time budget gauge, coverage radar for UDL/standards).
•
Data/state: TanStack Query for server cache; Zustand for editor cursors, section selection, timer sliders.
•
Realtime: WebSocket client (auto‑reconnect/backoff) + SSE fallback.
•
Tables: virtualized (questions, materials, gradebook).
•
File handling: signed S3 URLs for exports.
5.2 App Structure
/app /(marketing)/page.tsx /(app) dashboard/page.tsx units/ new/page.tsx [unitId]/ page.tsx lessons/
new/page.tsx [lessonId]/ page.tsx // Overview & status objectives/page.tsx sequence/page.tsx vocab/page.tsx activity/page.tsx quiz/page.tsx inserts/ history/page.tsx math/page.tsx science/page.tsx udl/page.tsx approvals/page.tsx exports/page.tsx admin/audit/page.tsx /components BriefWizard/* ObjectiveEditor/* TimeBudgetGauge/* SectionBuilder/* MaterialsList/* FormativeCheckList/* VocabTable/* MisconceptionList/* ActivityDesigner/* SafetyChecklist/* QuizTable/* RubricEditor/* Gradebook/* HistorySlides/* MathProblemSet/* ScienceLabSheet/* UDLPanel/* ApprovalsPanel/* ExportHub/* CommentThread/* /lib api-client.ts
ws-client.ts zod-schemas.ts rbac.ts /store useLessonStore.ts useEditorStore.ts useRealtimeStore.ts
5.3 Key Pages & UX Flows
Dashboard
•
Tiles: “Start lesson,” “In review,” “Ready to export.”
•
KPI chips: time budget fit, UDL coverage, approval status.
Objectives
•
BriefWizard intake; ObjectiveEditor shows objective + success criteria with Bloom tags; one‑click “rewrite for Grade 6 reading level”.
Sequence
•
TimeBudgetGauge visualizes minutes vs. period length; SectionBuilder reorderable sections with transitions; FormativeCheckList ensures at least one check/section.
Vocabulary & Misconceptions
•
VocabTable add/edit terms & kid‑friendly defs; MisconceptionList with correction sentence stems.
Activity
•
ActivityDesigner drop‑downs: lab/build/discussion; auto‑fills steps & group roles; MaterialsList with quantities; SafetyChecklist with PPE toggles.
•
Toggle “Equipment‑limited” for alternate pathway.
Quiz
•
QuizTable shows items with types, stems, choices, keys; RubricEditor for open responses; Gradebook quick‑entry grid & CSV export.
Inserts
•
HistorySlides: preview 6–10 MDX slides + source prompts.
•
MathProblemSet: dataset viewer, problems (core/challenge) + solutions toggle.
•
ScienceLabSheet: variables, controls, data table, analysis questions.
UDL
•
UDLPanel shows flags (reading level, scaffolds, visuals); “apply rewrite” chips; coverage radar.
Approvals
•
ApprovalsPanel: define chain; approve/reject with comment; lock after final approval.
Exports
•
ExportHub: pick artifacts (pack_pdf, slides_pdf, worksheets_pdf, quiz_pdf, csv_grades, bundle_zip); progress with signed URLs.
5.4 Component Breakdown (Selected)
•
SectionBuilder/Row.tsx
Props: { section, onChange }; minute spinner with guard (cannot exceed remaining); transition note field; formative check toggle.
•
ActivityDesigner/Step.tsx
Props: { index, text, timeMin? }; keyboard reorder; safety icon if step involves heat/sharp tools.
•
QuizTable/ItemRow.tsx
Props: { item }; supports MCQ/MS/numeric/short/label; validation (at least 3 choices for MCQ); answer/rubric editors.
•
UDLPanel/FlagRow.tsx
Props: { severity, message, rewrite }; “apply rewrite” button patches content in place.
•
Gradebook/Cell.tsx
Props: { studentAlias, itemId, points, onChange }; auto‑save debounce; keyboard navigation.
5.5 Data Fetching & Caching
•
Server Components for lesson snapshots, sections list, quiz items, inserts, approvals, exports.
•
TanStack Query for mutations and streamed results (drafting, UDL flags, export progress).
•
WS pushes patch editor state & lists via queryClient.setQueryData; optimistic UI for non‑destructive edits.
•
Prefetch neighbors: objectives → sequence → activity/quiz → inserts → udl → approvals → exports.
5.6 Validation & Error Handling
•
Zod schemas: objectives, sections, vocab, misconceptions, activity, safety, quiz items, rubrics, grades, approvals.
•
Problem+JSON renderer with remediation (e.g., “Time budget over by 6 minutes; reduce two sections or extend days”).
•
Guardrails:
o
Approval disabled if time budget mismatch or no formative check exists.
o
Activities require safety checklist entry to proceed.
o
Quiz export disabled if any item missing points or answer.
5.7 Accessibility & i18n
•
Keyboard‑first editing; ARIA roles for tables/editors; focus‑visible rings.
•
High‑contrast; color‑blind‑safe charts; projector‑mode font scaling.
•
next-intl scaffolding; reading level display; metric/imperial toggles.
6) Integrations
•
Storage: Google Drive/SharePoint (optional) for exports.
•
Rosters: CSV import (student aliases only by default).
•
Calendars: ICS export for lesson day schedules.
•
LMS: generic CSV exports; (optional later) webhooks for assignment creation—disabled by default to avoid permissions sprawl.
•
Comms: Email to self with pack links; Slack notifications for approvals/export ready.
•
Billing: Stripe (seats + metered generations).
7) DevOps & Deployment
•
FE: Vercel (Next.js 14).
•
APIs/Workers: Render/Fly.io or GKE (CPU pool for generation, mem‑opt for export jobs).
•
DB: Managed Postgres + pgvector; PITR; migration gates.
•
Cache: Upstash Redis.
•
Object Store: S3/R2 with lifecycle (retain exports; purge temp).
•
Event Bus: NATS (managed/self‑hosted).
•
CI/CD: GitHub Actions — lint/typecheck/unit/integration; Docker build; SBOM + cosign; blue/green deploy; migration approvals.
•
IaC: Terraform modules (DB, Redis, NATS, buckets, secrets, DNS/CDN).
•
Testing
o
Unit: timing allocator, quiz builder constraints, rubric scoring, UDL checks, safety gate.
o
Contract: OpenAPI.
o
E2E (Playwright): brief→objectives→sequence→activity/quiz→inserts→UDL→approvals→export.
o
Load: k6 (parallel lessons building & exporting).
o
Chaos: zero‑equipment path, extended periods, grades backfill.
o
Security: ZAP; container/dependency scans; secret scanning.
•
SLOs (restate)
o
Sequence <3s; Quiz <4s; Activity <3s; UDL <2.5s; Export <10s; WS P95 <250ms; 5xx <0.5%/1k.
8) Success Criteria
Product KPIs
•
Time‑to‑teachable lesson ≤ 15 min median from intake.
•
UDL coverage: ≥ 80% lessons pass with ≤2 low‑severity flags.
•
Assessment readiness: ≥ 10 well‑formed quiz items per lesson on average.
•
Teacher satisfaction: ≥ 4/5 rating on clarity & classroom practicality.
•
Export reliability: ≥ 99% successful artifact deliveries.
Engineering SLOs
•
Editor local echo < 80 ms; WS reconnect < 2 s P95; export failure rate < 1%.
9) Security & Compliance
•
RBAC: Owner/Admin/Teacher/Coach/Lead/Viewer; approvals gate publishing.
•
Encryption: TLS 1.2+; AES‑256 at rest; KMS‑wrapped secrets; signed URLs for exports.
•
Privacy (FERPA/COPPA/GDPR‑K aware): default to pseudonymous student IDs; no birthdates/emails/addresses required; configurable retention & deletion; DSR endpoints for org admins.
•
Tenant isolation: Postgres RLS; S3 prefix isolation.
•
Auditability: immutable audit_log for content generations, edits, approvals, exports.
•
Supply chain: SLSA provenance; image signing; pinned deps & vulnerability scanning.
•
Safety: activity steps include safety checklist; hazardous materials excluded by design.
10) Visual/Logical Flows
A) Intake → Objectives
Teacher enters brief → intake-normalizer → objective-writer outputs objectives & success criteria.
B) Sequence & Time Budget
sequence-planner creates minute‑by‑minute plan → teacher tweaks → time budget locked.
C) Inserts & Depth
History/Math/Science agents add their parts; Science builds lab sheet; Math builds datasets & problems; History creates slides/prompt.
D) Activity & Assessment
activity-designer crafts the hands‑on task with safety; quiz-builder produces items + keys; rubrics added.
E) UDL Review & Approvals
udl-checker flags & rewrites; Coach/Lead approval chain passes.
F) Exports
reporter/exporter compile Lesson Pack, Slides, Worksheets, Quiz, Gradebook, Bundle → signed links delivered.