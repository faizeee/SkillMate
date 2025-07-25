# 🗕️ Day 8 – Protected Routing, Toasts, and Error Handling

---

## 🔐 Authentication & Routing with TanStack Router

### ✅ Public vs Authenticated Layouts

* Introduced `PublicLayout.tsx` and `AuthLayout.tsx` (default layout for logged-in users).
* Ensured routing logic is clean and role-aware.

### 🔒 `beforeLoad` Auth Guard

* Used `beforeLoad` on `authenticatedLayoutRoute` to protect private routes.
* Redirects to `/login` if user is not authenticated.

```tsx
beforeLoad: async () => {
  const isLoggedIn = useAuthStore.getState().is_loggedin();
  if (!isLoggedIn) throw redirect({ to: "/login" });
}
```

### 🔁 Public Route Redirection

* If already logged in, redirect from `/login` back to `/`.

```tsx
useEffect(() => {
  if (is_loggedin()) navigate({ to: "/" });
}, []);
```

---

## 🧠 Zustand Auth Store Enhancements

### ✅ SSR-Safe Token Access

* Fixed SSR error by guarding `localStorage` reads:

```ts
const is_loggedin = () => {
  if (typeof window === "undefined") return false;
  return !!localStorage.getItem("token");
};
```

### ✅ Centralized Login Handling

* Moved login logic inside `performLogin()` action in `useAuthStore`.

```ts
performLogin: async (user) => {
  const response = await loginUser(user);
  setAuth(response); // sync to store + localStorage
},
```

---

## 🧪 AddSkillPage UX Polishing

### ✅ Skill Submission Enhancements

* Added loading state, reset after submit, and input validation.

```tsx
if (!name.trim()) return setError("Skill name required");
setIsSubmitting(true);
await addSkill({ name, level });
resetForm();
```

### ✅ Better Error Messages & API Handling

* Improved API error parsing:

```ts
const err_data = await response.json();
const err_message = err_data?.detail?.message || "Something went wrong";
set({ error: err_message });
throw new Error(response.status === 409 ? "Skill Already Exists" : err_message);
```

---

## 🔔 Toast Notifications (via `sonner`)

### ✅ Installed and configured sonner

```bash
npm install sonner
```

### ✅ Added `<Toaster />` globally

* In `main.tsx`:

```tsx
import { Toaster } from "@/components/ui/sonner";
<Toaster richColors position="top-right" />;
```

OR

* In both layouts: `PublicLayout` and `AuthLayout`.

### ✅ Show Toast on Success/Error

```tsx
import { toast } from "sonner";

toast.success("Skill added successfully");
toast.error(error.message || "Failed to add skill");
```

---

## 🧼 Code Cleanup & Refactors

* Used `useAuthStore.getState().token` instead of raw `localStorage.getItem('token')` in API calls.
* Introduced default props and boolean prop syntax for testing.

```tsx
function MyButton({ big = false }: { big?: boolean }) {
  return <button className={big ? "text-2xl" : "text-sm"}>Click</button>;
}
```

---

## ✅ Summary

* Implemented secure routing and redirection with TanStack Router.
* Polished AddSkillPage UX with better form handling.
* Global toast notifications with sonner.
* Robust error parsing from backend.
* Auth state consistency improved using Zustand.
* Code cleanup and best practices applied.

---
