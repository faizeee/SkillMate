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

## 📅 Daily Goal

We’re building one job-ready feature or setup milestone per day. Stay tuned.
