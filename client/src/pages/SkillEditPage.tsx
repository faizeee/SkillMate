// import { useEffect, useState } from "react";
import { useSkillsStore } from "../store/useSkillStore";
import { useLoaderData, useNavigate } from "@tanstack/react-router";
import { toast } from "sonner";
import type { NewSkill } from "@/types/skill";
import CreateSkillForm from "@/components/CreateSkillForm";
import { EditSkillRoute } from "@/router/skills/edit";

export default function SkillEditPage() {
  // const [skillData, setSkillData] = useState<NewSkill>({name:"",skill_level_id:""});
  const { updateSkill, loading } = useSkillsStore();
  const { skill: editSkill } = useLoaderData({ from: EditSkillRoute.id });
  const navigate = useNavigate();
  const handleSubmit = async (formData: NewSkill) => {
    console.info({ formData });
    try {
      await updateSkill(formData, editSkill.id);
      toast.success("New Skill Updated", {
        description: `${editSkill.name} was updated.`,
        action: {
          label: "Back to Skills Page",
          onClick: () => {
            console.info("redirecting to skills page");
            navigate({ to: "/skills" });
          },
        },
      });
    } catch (err) {
      toast.error(`${err || "Something went wrong"}`);
    }
  };

  return (
    <CreateSkillForm
      onSubmit={handleSubmit}
      editSkill={editSkill}
      loading={loading}
    />
  );
}
