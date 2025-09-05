## 🗓️ Day 20 – Skill Update, Delete & File Upload

### ✅ Goals
- Implement Edit (Update) Skill: backend + frontend
- Integrate Delete Skill (frontend only)
- Add File Upload functionality for skill images

### 🚀 Achievements

#### ✅ Update
- PATCH `/api/skills/{id}` route implemented
- Added role-based access check (owner/admin)
- Pre-filled edit form with toast + redirect
- Tests added for authorized/unauthorized edits

#### ✅ Delete
- Frontend-only delete with Axios + toast
- Integrated confirm prompt + UI refresh

#### ✅ Upload
- Created `/api/skills/{id}/upload` endpoint
- Saved files to `uploads/` folder
- Updated DB with image URL
- Upload form and preview on frontend
- Displayed images in skill cards

That's a great approach to capturing the essence of the work without focusing on the debugging process. A good commit message should tell a story about the change, explaining the "what" and the "why."

Here's a summary tailored to your request, focusing on the creation and purpose of the new components.

-----

### feat: Introduce robust auth flow with fetch wrapper and redirect hook

This commit establishes a new pattern for handling authentication throughout the application.

- **`fetchWithAuth` Wrapper:** Created a centralized `fetch` utility that automatically injects the user's authentication token into the headers. This wrapper also globally handles `401 Unauthorized` responses by clearing the token and triggering a logout, ensuring a consistent and secure state.

- **`useAuthRedirect` Hook:** Developed a custom React hook to manage client-side redirects based on the authentication state. This hook simplifies the process of protecting pages by automatically navigating users to the login screen if their token is missing.

- **Zustand Store:** Integrated a simple Zustand store to manage the token and authentication state, providing a single source of truth for the entire application.

These changes separate authentication concerns from the business logic, making the codebase more modular, scalable, and easier to maintain.

### FastAPI Static Files Configuration ⚙️

Even with a correct URL, the image was not found because FastAPI was not configured to serve files from the uploads directory. The solution was to use app.mount to tell the application to treat the static directory as a public web asset, allowing files within it to be served to the frontend.

### Feat: Add robust file I/O error handling for skill uploads 📁

This commit introduces comprehensive error handling for file I/O operations when uploading a new skill.

Previously, the application might have failed to provide a meaningful response to the user for low-level file system errors. This change adds logic to correctly translate OSError exceptions (e.g., errno.ENOSPC for disk full, errno.EACCES for permission denied) into appropriate HTTP status codes and user-friendly messages.

The changes were validated with a new parameterized test that uses pytest-asyncio and monkeypatch to simulate various I/O errors without requiring an actual file system. The FakeFile class was created for this purpose, which raises specific OSError exceptions to verify the API's response.

This ensures the application is more resilient and provides clear feedback to users when file-related issues occur.

### feat(skill): complete skill CRUD with file upload integration

- Added file upload support directly in skill create/update routes
- Introduced reusable file validation and storage utilities
- Refactored form parsing with get_skill_in dependency
- Enforced admin-only update/delete rules for skills
- Improved test stability and error handling


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



### 🔄 Next Steps
- Day 21: UI polish and validation on forms
- Start frontend unit tests for Skill components
- Add drag-and-drop upload (optional)
