import {
  createRootRoute,
  createRoute,
  createRouter,
  Outlet,
  redirect,
} from "@tanstack/react-router";
import { lazy } from "react";
import { useAuthStore } from "@/store/useAuthStore";

import Layout from "@/layouts/Layout";
import PublicLayout from "@/layouts/PublicLayout";
import LoginPage from "@/pages/LoginPage";
import AdminLayout from "@/layouts/AdminLayout";
import { EditSkillRoute } from "./skills/edit";
// Lazy-loaded pages
const SkillsPage = lazy(() => import("@/pages/Skills"));
// const AddSkillPage = lazy(() => import("@/pages/AddSkill"));
const SkillCreatePage = lazy(() => import("@/pages/SkillCreatePage"));
const HomePage = lazy(() => import("@/pages/Home"));
const ProfilePage = lazy(() => import("@/pages/Profile"));
const Dashboard = lazy(() => import("@/pages/admin/Dashboard"));

// Define the absolute root route of your application.
// This route acts as the highest common ancestor for all other routes.
// It might render a very basic wrapper or nothing, depending on your app's overall structure.
// For simplicity, let's make it render an <Outlet /> to immediately render its children.
const rootRoute = createRootRoute({
  component: Outlet,
});

// Define a child route of the main root for routes that use your main Layout and require auth
export const authenticatedRootRoute = createRoute({
  getParentRoute: () => rootRoute,
  component: Layout,
  id: "authenticated-root",
  // IMPORTANT: Use beforeLoad here for primary authentication check
  beforeLoad: async () => {
    // Access the auth state directly from the store (not via hook, as beforeLoad is not a React component)
    const is_loggedin = useAuthStore.getState().is_loggedin();
    if (!is_loggedin) {
      // If not logged in, redirect to the login page immediately.
      // This prevents the Layout or any child components from rendering.
      throw redirect({ to: "/login" });
    }

    // If logged in, proceed to render the Layout and its children.
    return {}; // Must return an object
  },
});
const adminRootRoute = createRoute({
  getParentRoute: () => rootRoute,
  component: AdminLayout,
  id: "admin-root",
  beforeLoad: async () => {
    const is_loggedin = useAuthStore.getState().is_loggedin();
    const role = useAuthStore.getState().user?.role?.title
    if (!is_loggedin) {
      throw redirect({ to: "/login" });
    }

    if (role != "Admin") {
      throw redirect({ to: "/unauthorized" })
    }


    // If logged in, proceed to render the Layout and its children.
    return {}; // Must return an object
  },
});
// Public Root Route
const publicRoute = createRoute({
  getParentRoute: () => rootRoute,
  component: PublicLayout,
  id: "public-root",
});

const public_routes = publicRoute.addChildren([
  createRoute({
    path: "/login",
    getParentRoute: () => publicRoute,
    component: LoginPage,
  }),
  // Add other public routes like /register, /forgot-password here
]);

// Authenticated routes (children of authenticatedRootRoute)
// These routes will first go through authenticatedRootRoute's beforeLoad
const authenticated_routes = authenticatedRootRoute.addChildren([
  createRoute({
    path: "/",
    getParentRoute: () => authenticatedRootRoute,
    component: HomePage,
  }),
  createRoute({
    path: "/skills",
    getParentRoute: () => authenticatedRootRoute,
    component: SkillsPage,
  }),
  createRoute({
    path: "/add",
    getParentRoute: () => authenticatedRootRoute,
    component: SkillCreatePage,
  }),
  EditSkillRoute,
  createRoute({
    path: "/profile",
    getParentRoute: () => authenticatedRootRoute,
    component: ProfilePage,
  }),
]);

const admin_routes = adminRootRoute.addChildren([
  createRoute({
    path: "/admin/",
    getParentRoute: () => adminRootRoute,
    component: Dashboard,
  })
]);

const routeTree = rootRoute.addChildren([public_routes, authenticated_routes,admin_routes]);

// ✅ Export the router instance
export const router = createRouter({ routeTree });

// ✅ Also declare module for type safety
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

// // Ensure the router is rendered in your root application component
// const rootElement = document.getElementById('app')!;
// if (!rootElement.innerHTML) {
//   const root = createRoot(rootElement);
//   root.render(
//     <StrictMode>
//       <RouterProvider router={router} />
//     </StrictMode>
//   );
// }
