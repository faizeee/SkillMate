// import { useEffect, useState } from "react";
import { useSkillsStore } from "../store/useSkillStore";
import { useNavigate } from "@tanstack/react-router";
import { toast } from "sonner";
import type { NewSkill } from "@/types/skill";
import CreateSkillForm from "@/components/CreateSkillForm";

export default function SkillCreatePage() {
  // const [skillData, setSkillData] = useState<NewSkill>({name:"",skill_level_id:""});
  const { addSkill, loading } = useSkillsStore();
  const navigate = useNavigate();
  const handleSubmit = async (formData: NewSkill) => {
    console.info(formData);
    try {
      await addSkill(formData);
      toast.success("New Skill Added",{
        description:"New skill is added to database",
        action:{
          label:"Go to Skills Page",
          onClick: ()=>{
            console.info("redirecting to skills page");
            navigate({ to: "/skills" });
          }
        }
      });
      // ✅ Only navigate if no error
      //
    } catch (err) {
      toast.error(`${err || "Something went wrong"}`);
    }
  };

  return <CreateSkillForm onSubmit={handleSubmit} loading={loading} />;
}
