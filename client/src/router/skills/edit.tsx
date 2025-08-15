import { createRoute } from "@tanstack/react-router";
import { lazy } from "react";
import { authenticatedRootRoute } from "..";
import { useSkillsStore } from "@/store/useSkillStore";
const SkillEditPage = lazy(() => import("@/pages/SkillEditPage"));
export const EditSkillRoute = createRoute({
  path: "/edit/$skillId",
  getParentRoute: () => authenticatedRootRoute,
  component: SkillEditPage,
  loader: ({ params }) => {
    console.log(params);
    const skill = useSkillsStore.getState().getSkill(params.skillId);
    console.log(skill);
    return {skill};
  },
});
