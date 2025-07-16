import {
  createRootRoute,
  createRoute,
  createRouter,
  RouterProvider,
} from "@tanstack/react-router";
import { lazy, StrictMode } from "react";
import { createRoot } from "react-dom/client";

import Layout from "@/layouts/Layout";
import HomePage from "@/pages/Home";
import SkillsPage from "@/pages/Skills";
import AddSkillPage from "@/pages/AddSkill";
import LoginPage from "@/pages/LoginPage";
import ProfilePage from "@/pages/Profile";
// Define root layout with children pages
const rootRoute = createRootRoute({
  component: Layout,
});

const routeTree = rootRoute.addChildren([
  
  createRoute({
    path:"/login",
    getParentRoute: ()=>rootRoute,
    component:LoginPage
  }),
  createRoute({
    path: "/",
    getParentRoute: () => rootRoute,
    component: HomePage,
  }),
  createRoute({
    path: "/add",
    getParentRoute: () => rootRoute,
    component: AddSkillPage,
  }),
  createRoute({
    path: "/skills",
    getParentRoute: () => rootRoute,
    component: SkillsPage,
  }),
  createRoute({
    path: "/profile",
    getParentRoute: () => rootRoute,
    component: ProfilePage,
  }),
]);

// ✅ Export the router instance
export const router = createRouter({ routeTree });

// ✅ Also declare module for type safety
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}
