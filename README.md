# SkillMate – Learn & Teach Platform

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


## 📅 Daily Goal

We’re building one job-ready feature or setup milestone per day. Stay tuned.
