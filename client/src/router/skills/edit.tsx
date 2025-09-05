import { createRoute, notFound } from "@tanstack/react-router";
import { lazy } from "react";
import { authenticatedRootRoute } from "..";
import { useSkillsStore } from "@/store/useSkillStore";
const SkillEditPage = lazy(() => import("@/pages/SkillEditPage"));
export const EditSkillRoute = createRoute({
  path: "/edit/$skillId",
  getParentRoute: () => authenticatedRootRoute,
  component: SkillEditPage,
  loader: async  ({ params }) => {
    console.log(params);
    const skill = await useSkillsStore.getState().fetchSkill(params.skillId);
    console.log(skill);
    if(!skill) {
        throw notFound()
    }
    return {skill};
  },
});
