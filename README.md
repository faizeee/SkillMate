# Testing GitHub CI + Codecov

# SkillMate – Learn & Teach Platform

![CI](https://github.com/faizeee/skillmate/actions/workflows/ci.yml/badge.svg)
[![Backend Coverage](https://codecov.io/gh/faizeee/SkillMate/branch/main/graph/badge.svg?flag=backend)](https://codecov.io/gh/faizeee/SkillMate)
[![Frontend Coverage](https://codecov.io/gh/faizeee/SkillMate/branch/main/graph/badge.svg?flag=frontend)](https://codecov.io/gh/faizeee/SkillMate)

SkillMate is a full-stack platform where users can **offer** or **learn** real-world skills — from cooking and coding to photography and design. This project demonstrates a complete production-grade stack with modern frontend and backend technologies.

## 🔧 Tech Stack

- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Backend:** FastAPI, PostgreSQL
- **DevOps:** Docker, GitHub Actions

## 🛠️ Features (Planned)

- User Registration & Login (JWT)
- Skill Listings & Search
- Booking / Request Sessions
- Reviews & Ratings
- Admin Panel

## 🎯 Purpose

This project is part of a personal initiative to become job-ready for remote full-stack roles by building a complete application from scratch using modern tools.

# SkillMate

SkillMate is a full-stack platform to help users manage, showcase, and track their learning journey and skills.

## 💻 Tech Stack

- **Frontend**: React, TypeScript, Tailwind CSS, Vite
- **Backend**: FastAPI (Python)
- **Dev Tools**: ESLint, Prettier, VS Code, GitHub

![CI](https://github.com/faizeee/skillmate/actions/workflows/ci.yml/badge.svg)
---

## 🚀 Progress Log

### ✅ Day 1: Project Setup (Frontend + Backend)

- Initialized full-stack project: `SkillMate`
- Set up React + TypeScript + Vite in `/client`
- Installed and configured Tailwind CSS v4
- Added ESLint with Airbnb + Prettier integration
- Created FastAPI backend in `/backend`
- Created and tested root API route (`GET /`)
- Confirmed backend is running on `http://localhost:8000`

### ✅ Day 2: Routing + Tailwind Integration

- Added **TanStack Router** with base layout and pages
  - Created `/`, `/skills`, and `/profile` routes
  - Setup `RootLayout` with sidebar navigation
- Fixed Vite + Tailwind 4 integration issues
  - Added `tailwind.config.js` with correct `content` paths
  - Cleaned up `index.css` to prevent default style conflicts
- Verified Tailwind utility classes are rendering correctly
  - Example: `text-4xl text-green-400 font-bold`
- Rendered sample content on `HomePage` for testing Tailwind output
- Confirmed routing and layout working via `npm run dev`

### ✅ Day 3: Global Store + API Data Rendering

- Created `useSkillStore.ts` with Zustand for global skill state
  - Manages `skills`, `loading`, `error`
  - Added async `fetchSkills()` method
- Connected frontend to FastAPI with `GET /api/skills`
- Displayed skills on the `/skills` route with Tailwind styling
- Rendered loading/error UI states
- Fixed rendering bug by correctly returning JSX inside `.map()`
- Confirmed frontend is fully API-driven now 🚀

### ✅ Day 4: Zustand Integration + Add Skill Form

- ✅ Integrated [**Zustand**](https://github.com/pmndrs/zustand) for global state management
- ✅ Created a `useSkillsStore.ts` to manage:
  - `skills` state
  - `loading` and `error` flags
  - an async `fetchSkills()` function using a reusable fetch wrapper
- ✅ Defined `Skill` and `NewSkill` types with proper type safety
- ✅ Built the `AddSkillPage` component with:
  - Form inputs for `name` and `level`
  - A submit handler to call `addSkill()` and navigate to `/skills`
  - Basic client-side validation (`name` required)
- ✅ Implemented a reusable fetch wrapper to simplify API handling
- ✅ Discussed and planned for:
  - Showing backend validation errors in the form
  - Redirecting only on successful submission
  - Optional `Skill` type merging with `NewSkill`
  - Moving base URL to a central constants file
- ✅ App now supports adding a new skill via FastAPI and viewing updated skill list

### ✅ Day 5: Backend Refactor, Controllers, and API Architecture

- ✅ **Modularized backend structure** for scalability and maintainability
- ✅ Created a dedicated `controllers/` folder and moved business logic there
- ✅ Separated model definitions into `models/skill/`:
  - `SkillIn` for incoming data (input)
  - `Skill` for response with `id`
- ✅ Extended `Skill` from `SkillIn` to keep input/output clean and DRY
- ✅ Created `routes/api/skill.py` for all skill-related routes
- ✅ Created centralized API router in `routes/api/index.py`
- ✅ Mounted API in `main.py` with prefix `/api` using:
  ```python
  app.include_router(api_router, prefix="/api")
🔧 Utilities & Validation

    ✅ Created utils/validation.py for:

        allowed_levels() — central allowed levels list

        check_duplicate_skill_name(name: str) — checks for existing skill names (case-insensitive)

    ✅ Added custom field validators using @validator:

        Ensured level is in allowed values

        Trimmed name and level before validation using pre=True

⚙️ Middleware

    ✅ Created custom logging middleware:

        Logs every request method, path, and total process time

        Added using FastAPI's BaseHTTPMiddleware

 ### ✅ Day 6: JWT Auth Backend Setup (FastAPI)

- 🔒 Created modular auth routes in `routes/api/auth_router.py`
- ✅ Defined request & response models in `models/user/schema.py` and `models/base/auth_response.py`
- 🧠 Added input validation using Pydantic (`min_length`, `no_spaces`, etc.)
- 📂 Moved business logic into `controllers/auth_controller.py`
  - Implemented `/register` route with password hashing and duplicate username check
  - Implemented `/login` route with password verification and JWT creation
- 🔐 Setup JWT utility functions in `core/auth.py`
- 🧪 Protected `POST /skills` route using `Depends(get_current_user)`
- 🧼 Organized route registration in `routes/api/index.py`
- 📁 Maintained clean package structure across models, routes, controllers, and services
### ✅ Day 7: Authentication, ORM Mastery & Backend Enhancements

#### 🔐 Frontend Authentication (React + Zustand)
- Created `LoginPage` with controlled inputs for username and password
- Implemented basic form validation on client
- Connected login form to FastAPI `POST /api/login` endpoint
- Created `useAuthStore` with Zustand to manage auth state
  - Stored JWT token and username in `localStorage`
  - Added logout function to clear state and storage
- Updated UI to show current logged-in user
- Redirected user to `/skills` page after successful login

---

#### 🧠 Backend Improvements (FastAPI + SQLModel)

- **📦 Refactored Route & Controller Structure**
  - Moved auth logic to `controllers/auth_controller.py`
  - Created separate model for `AuthResponse` with helper method
  - Used clean and type-safe request/response typing across endpoints
  - Organized routes: `routes/api/auth_router.py`

- **🌱 Separated DB Seeding Logic**
  - Moved seeding from `data/db.py` to `seeders/seed.py`
  - Cleaner architecture and single responsibility

- **🔁 Resolved Circular Import Issues**
  - Handled import errors between `Skill` and `SkillLevel` models
  - Used `update_forward_refs()` in `data/models/__init__.py`
  - Consolidated model imports with a clear API surface

- **⚡ Eager Loading for Relationships**
  - Used `selectinload` to load `SkillLevel` data efficiently with `Skill`
  - Prevented N+1 query problem during DB access

- **🐍 Pythonic Data Transformation**
  - Converted SQLModel object lists to dicts using list comprehensions
    ```python
    skills = [skill.to_dict() for skill in result]
    ```

- **λ Mastered Lambda Functions**
  - Used lambdas for inline sorting and data filtering
    ```python
    sorted_skills = sorted(skills, key=lambda s: s.name)
    ```

- **🧩 Improved Query Construction**
  - Adopted multi-step, readable SQLModel query pattern:
    ```python
    stmt = select(Skill).where(Skill.level_id == 2)
    skills = db.exec(stmt).all()
    ```

- **🛡️ Enforced DB-Level Unique Constraints**
  - Checked duplicate `Skill.name` via DB query
  - Explained why `@validator` isn't suitable for DB-based logic

- **🐛 Fixed Validation Mistake**
  - Debugged `min_length` TypeError for an integer (`level_id`)
  - Learned that `min_length` only applies to string fields

- **🔄 Refreshed Related Data on Commit**
  - Used `db.refresh(obj, attribute_names=["relation"])` after creating `Skill`
  - Ensured that nested relations like `Skill.level` are immediately available

---

🔥 **Reflection**: This was a real engineer's day. You cleaned architecture, handled DB relations like a pro, solved real-world bugs, and built solid auth. You're not just building apps now — you're building systems.
# 📅 Day 8 – UX Polish, Auth Routing, Error Handling, Toast System

Today we focused on ([→ Full Details](logs/day-8.md)):
- Protected routing with `beforeLoad` and TanStack Router
- Public vs Auth layouts
- SSR-safe localStorage access
- Improved login flow (via `performLogin` in Zustand)
- Fixed auth state sync issues (read from localStorage)
- AddSkillPage UX polish (validation, loading, reset)
- Global toast system with `sonner`
- Graceful error handling + proper Authorization header

# 📘 SkillMate – Day 9: Backend Testing Begins 🧪

Today we introduced backend testing using **pytest** with an isolated in-memory SQLite database. Our main goal was to set up a clean testing structure and validate our first endpoint: `GET /api/skills`.

---

## ✅ Accomplishments

- ✅ Set up **pytest** for the FastAPI backend
- ✅ Created a test-only in-memory SQLite DB
- ✅ Built `tests/conftest.py` with test client and fixtures
- ✅ Added a `seed_test_db()` to populate skill levels and skills
- ✅ Wrote and passed our **first test** for `GET /api/skills`
- ✅ Learned how to override dependencies using FastAPI’s `app.dependency_overrides`

---

## 🔧 `tests/conftest.py`

- Creates in-memory SQLite DB
- Overrides production DB dependency
- Seeds skills + levels
- Drops schema after all tests complete

# 📘 Day 10 – Backend Testing Complete (Users + Skills API)

---

## ✅ What We Accomplished

- 🔹 Finalized **sync-based API testing** using `pytest`
- 🔹 Added tests for:
  - 🔸 Skills (create, fetch, delete, validation, edge cases)
  - 🔸 Users (register, login, error handling)
- 🔹 Structured clean test files: `test_skills.py`, `test_users.py`
- 🔹 Created reusable test utilities in `utils/helpers.py`
- 🔹 Used `auth_headers` fixture to simplify skill tests

---

## 🧪 Skills API Tests (`tests/test_skills.py`)

- ✅ `test_get_skills`
- ✅ `test_create_skill`
- ✅ `test_create_duplicate_skill`
- ✅ `test_invalid_payload` (parametrized)
- ✅ `test_get_skill_by_valid_id`
- ✅ `test_get_skill_by_invalid_id`
- ✅ `test_delete_skill_by_valid_id`
- ✅ `test_skill_by_invalid_id`

---

## 🔐 User Auth Tests (`tests/test_users.py`)

- ✅ `test_register_user`
- ✅ `test_register_duplicate_user`
- ✅ `test_register_invalid_payload` (parametrized)
- ✅ `test_register_invalid_min_length_payload`
- ✅ `test_login_user`
- ✅ `test_login_invalid_password` (parametrized)
- ✅ `test_login_invalid_payload` (parametrized)

---

## ⚙️ Testing Utilities

- 🔸 File: `utils/helpers.py`
- 🔸 Function: `register_and_login_test_user(client)`
- 🔸 Returns valid `Authorization` headers for authenticated testing
- 🔸 Used in all skill-related tests via `auth_headers` fixture

---

## ⚡ Performance: Run Tests Faster

- 🔹 Install `pytest-xdist`:
  ```bash
  pip install pytest-xdist

# ✅ Day 11 – Backend Coverage & Testing Deep Dive

Today, we refined our backend test suite and inspected code coverage for key controller files.

## 🔍 Focus Areas
- Ran `pytest` with `coverage` to analyze test reach
- Investigated why controller methods (`auth_controller.py`, `skill_controller.py`) showed low coverage
- Identified that calling routes does **not automatically mark controller function bodies as covered**
- Ensured `.coveragerc` and project structure excludes `env/`, `__pycache__/`, and `.egg-info/` from scanning

## 📁 Observations
- Unexpected folders:
  - `env/` – virtualenv; ignore in version control
  - `skillmate_backend.egg-info/` – safe, created by editable installs
  - `build/` – safe, usually created by packaging tools

### 📈 Code Coverage Highlights

| ✅ **Overall**                                         | **92%**  |

# ✅ Day 12 — Fullstack Testing Progress (Pytest + Vitest)

**Focus:**
Write and improve **frontend unit tests** using Vitest & React Testing Library, and optimize **backend test coverage** with Pytest.

---

### ✅ Completed Frontend Tasks:

- 🧪 Integrated Vitest and React Testing Library for frontend testing
- 🔧 Mocked external dependencies:
  - Zustand stores: `useSkillsStore`, `useSkillLevelStore`
  - `@tanstack/react-router`'s `useNavigate`
  - `sonner` toast functions using `vi.hoisted()` to handle hoisting issues
- ✅ Fully tested UI form flow, rendering, error states, and success paths

---

### 🧪 Frontend Test Summary:

```bash
PASS  src/components/__tests__/SkillCard.test.tsx
 ✓ renders skill name and level

PASS  src/components/__tests__/SkillsList.test.tsx
 ✓ renders list of skills
 ✓ shows fallback message when no skills exist

PASS  src/components/__tests__/AddSkillPage.test.tsx
 ✓ renders form correctly
 ✓ shows error if name is empty
 ✓ submits valid form and navigates
 ✓ shows error toast if addSkill fails

Test Files  3 passed (3)
Tests       7 passed (7)
```
## ✅ Completed Backend Tasks:

* 🔍 Reviewed and identified uncovered code blocks
* ✍️ Wrote additional edge-case and empty-table tests
* 🧪 Optimized test coverage for API endpoints and validation paths

---

## Key Learnings:

* 🔁 Used `vi.hoisted()` to avoid mock hoisting issues with `vi.fn()`
* 🧪 Leveraged `waitFor()` and `findBy...` queries for async test cases
* ✅ Zustand state mocking makes React components easily testable

---

## 🚀 Backend coverage debugging builds confidence in API reliability

### ✅ Progress Recap:

* ✅ **Frontend**: 7 unit tests across 3 files — all passing
* ✅ **Backend**: Pytest coverage improved from ~80% → 97%
* 🧱 Stable foundation for CI (GitHub Actions) and deployment safety

## 🧠 Key Learnings

- Writing good tests is more than just hitting 100% — it's about covering **real usage paths**.
- **Fixture conflicts** and test data duplication can silently break expectations.
- The `coverage report` is your best friend for spotting the real gaps.


# ✅ Day 13 Progress – CI/CD & Environment Configuration

### 🔧 What We Did:
- ♻️ **Refactored `.env` management** for both backend and frontend
  - Separated environment variables cleanly
  - Used `vite`-prefixed variables for client
  - Used `python-dotenv` and `.env.example` for backend
- ⚙️ **Set up GitHub Actions CI pipelines**
  - ✅ Backend: `pytest` with 97%+ coverage
  - ✅ Frontend: `Vitest` with coverage reporting
  - Configured caching for faster CI builds
- 📦 Fixed CI errors by:
  - Ignoring `node_modules` and `package-lock.json` in workflows
  - Running `npm install` instead of `npm ci`
- 📈 Integrated **Codecov**
  - Auto-uploads coverage reports from GitHub Actions
  - PR comment support added (Codecov bot enabled)
  - Currently shows:
    - Backend: 98% coverage (`pytest --cov`)
    - Frontend: ✅ 100% patch coverage (Vitest)

---

### 📁 New or Updated Files
- `.env`, `.env.example`, `.env.test`, `.env.production`
- `.github/workflows/backend.yml`
- `.github/workflows/frontend.yml`
- `client/vite.config.ts`
- `backend/conftest.py`, `test.env`
- `README.md` (add Codecov badges next)

---

### 🧪 Coverage Status
- ✅ Backend: 97%+ total coverage
- ✅ Frontend: 100% patch coverage

# ✅ Day 14 - SkillMate Backend - Docker &  PostgreSQL Setup

> 💥 After 9 intense hours and 4+ hrs debugging volume issues — we finally have a working Dockerized FastAPI backend using **PostgreSQL** instead of SQLite! This README documents the working state as of **July 24**.

---

## ✅ Achievements [→ Full Details](logs/day-14.md):
- [x] ✅ Dockerized FastAPI app with `uvicorn`
- [x] ✅ Switched from SQLite → PostgreSQL
- [x] ✅ Dockerized PostgreSQL container with volume persistence
- [x] ✅ Seed DB script runs only once at container startup
- [x] ✅ `.env` configuration respected inside Docker
- [x] ✅ Verified API routes accessible at `http://localhost:8000`
- [x] ✅ Removed faulty volume mount (`.backend:/app/backend`)
- [x] ✅ Full image rebuild after cache purge (`1.6GB` reclaimed)

---

## 🐘 Database: PostgreSQL via Docker

### 📦 PostgreSQL Service (docker-compose.yml)

```yaml
services:
  db:
    image: postgres:15
    container_name: skillmate-db
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: skillmate_user
      POSTGRES_PASSWORD: supersecret
      POSTGRES_DB: skillmate_db
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```
# ✅ Day 15 Progress – SkillMate 🧠🚀 [→ Full Details](logs/day-15.md)

## 🔹 🐳 Docker Integration (Frontend + Backend)

- ✅ Created a `client/Dockerfile` using **Nginx** to serve Vite build output.
- ✅ Updated `docker-compose.yml`:
  - Connected frontend and backend containers via service names.
  - Mapped ports:
    - Frontend: `3000:80`
    - Backend: `8000:8000`
- ✅ Frontend running at: [http://localhost:3000](http://localhost:3000)
- ✅ Backend API docs at: [http://localhost:8000/docs](http://localhost:8000/docs)
- ✅ Verified JWT Auth flow is functional with PostgreSQL.

---

## 🛠️ 🔧 Docker Line Ending Fix (Windows Shell Script Issue)

We resolved a blocking Docker bug caused by **Windows-style line endings (`\r\n`)** in shell scripts.

### 🔸 Problem:
- Docker container failed with:
  `exec ./start.sh: no such file or directory`
  despite `start.sh` being present.

### 🔸 Root Cause:
- File had Windows-style CRLF endings, making `chmod +x` ineffective inside Linux container.

### ✅ Solution:
- Replaced `dos2unix` (which wasn't available) with:
  ```dockerfile
  RUN sed -i 's/\r$//' ./start.sh

# 📅 Day 16 – Stability, CI Cleanup & Pre-Commit Finalization [→ Full Details](logs/day-16.md)

🔹 Switched to Poetry for dependency management, cleaning up `requirements.txt` usage
🔹 Fixed Docker build errors caused by Python version incompatibilities (`fastapi-cache2`)
🔹 Removed Redis integration after multiple CI/test failures and focused on restoring stability
🔹 All tests now passing and coverage reported to Codecov
🔹 Pre-commit fully configured and running: `black`, `flake8`, `check-yaml/json`, etc.
🔹 Clean Dockerfile with proper shell script permission fixes (line endings, `chmod +x`)
🔹 GitHub Actions CI runs tests and uploads coverage for both backend and frontend
🔹 Protected `main` branch with enforced CI checks
🔹 Redis logic removed cleanly but retained in logs for future optional caching

✅ Everything is green, fast, and reliable — back on track for feature dev tomorrow!

# 📅 Day 17 – Dockerized PostgreSQL CI ✅, Deterministic Tests 🧪, Parallel Test Prep ⚙️

## ✅ Completed

- 🔁 **Migrated test database from SQLite → PostgreSQL**
- 🐳 **Integrated PostgreSQL with Docker Compose for both local & CI**
- ✅ **Enabled deterministic test seeding using `reset_test_db` + `run_migrations_and_seed_db`**
- ✅ **Overrode FastAPI `get_session` dependency with isolated `test_db_engine`**
- 🔒 **Used `filelock` to prevent parallel seeding/migration race conditions**
- 🧪 **All tests passing with full database reset where needed**
- 🟢 **CI fully green using PostgreSQL**
- ✅ **Added test coverage badge to `README.md`**
- ⚙️ **Started working on re-enabling `pytest-xdist` for parallel testing**
- ⚠️ **Observed flaky behavior during parallel runs (changing errors each time)**
- 🧠 **Implemented dynamic per-worker test DB creation using `PYTEST_XDIST_WORKER`**
- 🛠️ **Designed automatic worker DB cleanup after test sessions**
- 🐞 Investigated key errors:
  - Alembic migrations not applying in time (race condition)
  - `skill_levels`, `user_roles`, and other missing tables
  - Tests failing inconsistently across workers

## ⏱ Time Spent: ~6–9 hours

> 🧠 High-effort day — after nearly **5 days** of persistence, we now have **stable PostgreSQL CI & tests passing**. 🎉

---

# 📅 Day 18 – Role-Based Access Control (ACL) [→ Full Details](logs/day-18.md)

- ✅ Added `user_roles` table and seeded roles: `Admin`, `User`
- ✅ Added `role_id` foreign key to `users` table with default
- ✅ Built reusable permission dependency: `required_role`
- ✅ Created guards: `admin_only`, `user_only`
- ✅ Protected routes using role-based `Depends` checks
- ✅ Wrote full test suite for:
  - Permission dependencies
  - Protected routes using admin and user tokens
- ✅ Debugged and fixed route conflict issue in tests using unique paths
- ✅ Developed all logic and tests independently — huge confidence boost 🎉


---

## 🔧 Tech Highlights

- `--dist loadscope` performed better than `loadfile` in minimizing test collisions
- Used dynamic DB naming: `skillmate_test_db_<worker_id>` for isolation
- Added worker-aware debug logging using `os.getenv("PYTEST_XDIST_WORKER")`
- Detected `.env` syntax issues when running under xdist (dotenv couldn't parse)

---

## 💤 Blockers / Next Steps (moved to **Day 18**)

- 🧪 **Re-enable and stabilize `pytest-xdist`** with:
  - Safe per-worker DB setup
  - Alembic migration locking
  - Post-test DB teardown
- 🔐 **Implement ACL (Access Control Layer)**:
  - Add `user_roles` table
  - Add `user.role_id` foreign key
  - Protect routes via role-based checks

---

# 🚀 Day 19 – Frontend Role-Based Access Control (RBAC)

### ✅ Goals
- Implement UI-level access control using user roles from Zustand auth store
- Create `useRole` hook for easy access to current user’s role
- Conditionally render UI elements (e.g. buttons) based on role
- Protect sensitive pages using TanStack Router’s `beforeLoad` with role checks
- Write tests to verify role-based rendering using Zustand mocking

---

### 📁 Files Touched
- `src/hooks/useRole.ts` – new custom hook for accessing role
- `src/components/InviteMentorButton.tsx` – role-protected component
- `src/routes/admin/dashboard.tsx` – TanStack route with `beforeLoad` role check
- `src/components/__tests__/InviteMentorButton.test.tsx` – unit test with role mocking
- `test/utils/renderWithAuthRole.ts` – helper for rendering with mocked Zustand store

---

### 🧠 Key Concepts Implemented
- ✅ Zustand-based role access using `useAuthStore`
- ✅ React UI conditional rendering with `useRole()`
- ✅ `beforeLoad()` hook in TanStack Router to protect routes
- ✅ `act()` wrapping in tests to avoid React state update warnings
- ✅ Clean test isolation with store resets between tests

---

### 🧪 Sample Test Case
```tsx
act(() => {
  useAuthStore.setState({
    token: "mock-token",
    user: mockUser("admin"),
  })
})
render(<InviteMentorButton />)
expect(screen.getByText("Invite Mentor")).toBeInTheDocument()
```
# 🚀 Day 20 Milestone (Aug 6 → Sept 5)

Day 20 was planned as “just update/delete/file upload,” but it evolved into a **major architecture milestone**.
Instead of a quick feature tick, this month delivered **async support, robust file handling, better testing, and a more modular system design**.

---

## ⚙️ Backend Architecture
- Transitioned from **pure sync → async** routes and testing (big shift).
- Added **async test client setup**, laying groundwork for scalable async workflows.

---

## 🧪 Testing Improvements
- Used **pytest-mock** and **monkeypatching** effectively.
- Built **mock fixtures** for reuse across test suites.
- Leveraged **`tmp_path`** for isolated file tests.
- Added **`FakeFile`** helper to simulate I/O errors.
- Validated error mapping at **both utility-level and route-level** with `pytest-asyncio` and parametrized tests.

---

## 🗂️ File Handling
- Implemented **`save_file`** (async write) and **`save_file_safe`** (robust error translation).
- Added **file validation utility** (type/size checks, reusable).
- Created **form-to-pydantic converter** (`get_skill_in`) for clean route signatures.
- Introduced **asset utility** for generating absolute URLs to static resources.

---

## 🏗️ Domain Model Improvements
- Added **computed property** in `SkillRead` → `icon_url` dynamically generated.
- Enforced **admin-only update/delete** → simpler, safer auth model.
- Improved **DB modeling discussion** → avoiding duplication, preparing for many-to-many pivot.

---

## 🧩 Overall System Flow
- Reused the **same form for create & update** (DRY principle).
- Simplified **route signatures** via dependencies.
- Refactored request handling into **modular utilities**.

**Frontend restructured with:**
- `fetchWithAuth` wrapper (token injection + 401 logout)
- `useAuthRedirect` hook (protected routes)
- Zustand store for centralized auth state

---

## ⚡ Static Assets
- Configured **FastAPI `app.mount`** for serving `/uploads`.
- Integrated **icon URLs** via computed model property (`SkillRead.icon_url`).

---

## 🎯 Outcomes
- ✅ Async support across routes & tests
- ✅ Full file handling pipeline (validation → save → URL)
- ✅ Mocking & error simulation in tests
- ✅ Cleaner Pydantic model design (computed props, DRY schemas)
- ✅ Utility-based reusable architecture
- ✅ Simplified authorization model (admin-only updates/deletes)
- ✅ Frontend auth flow hardened with hooks + global wrapper




We’re building one job-ready feature or setup milestone per day. Stay tuned.
