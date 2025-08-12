import { createRoute } from "@tanstack/react-router";
import { lazy } from "react";
import { authenticatedRootRoute } from "..";
const SkillEditPage = lazy(() => import("@/pages/SkillEditPage"));
export const EditSkillRoute = createRoute({
  path: "/edit/:skill_id",
  getParentRoute: () => authenticatedRootRoute,
  component: SkillEditPage,
  loader: ({ params }) => {
    console.log(params);
    return { skill_id: params.skill_id };
  },
});
