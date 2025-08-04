# 📅 Day 18 – Implement Role-Based Access Control (ACL)

## 🏗️ Goals
- Create a `user_roles` table in the database
- Add `role_id` as a foreign key to the `users` table
- Seed initial roles: `Admin`, `User`
- Implement role-checking dependency: `required_role`
- Create reusable guards: `admin_only`, `user_only`
- Protect selected routes using these guards
- Write a test suite to verify permission enforcement

---

## ✅ Achievements

### 🗃️ Database Changes
- Created `user_roles` model with unique `title` field
- Added `role_id` to `users` table with FK to `user_roles`
- Default `role_id` is set to `User` during registration

### 🧩 Permissions System
- Created a generic `required_role(required_roles: str | list[str])` dependency
- Handles both single-role and multi-role checks dynamically
- Defined:
  - `admin_only = required_role("Admin")`
  - `user_only = required_role(["Admin", "User"])`

### 🔒 Protected Routes
- Used `Depends(admin_only)` and `Depends(user_only)` to enforce ACL
- Ensured only users with appropriate roles can access protected routes

### 🧪 Tests
- Created `test_permissions_dependency.py` to test:
  - ACL logic via direct dependency usage
  - Protected routes with various users (admin & regular)
- Ensured `403 Forbidden` is raised for unauthorized access
- Used JWT tokens in headers for simulated user roles
- Solved a bug where tests failed when run together due to route path conflicts:
  - Resolved by giving each test its own unique route path (e.g., `/test-acl/1`, `/test-acl/2`)

---

## 🧠 Reflection
> Today felt like a **level-up** in my backend skills. I designed and implemented role-based permissions completely on my own — from schema to API protection to writing meaningful tests. I also debugged complex route-related test issues confidently. This was the first time I felt like I don’t depend on anyone to code — I can think, build, test, and fix it all.

---

## 📝 Next Steps
- Add logging for permission-denied attempts
- Optionally assign roles dynamically via admin route
- Add per-resource permissions like `can_edit_post`, `can_manage_users`
