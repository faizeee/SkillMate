import { useRole } from "@/hooks/useRole";
import { useSkillsStore } from "@/store/useSkillStore";
import type { Skill as SkillType } from "@/types/skill";
import { Link } from "@tanstack/react-router";
import { toast } from "sonner";

type SkillProps = {
  skill: SkillType;
  // onDeleteSkill ?: (skill_id: number | string)=>void
};

const SkillCard = ({ skill }: SkillProps) => {
  const handelDeleteSkill = async () => {
    const skill_name = `${skill.name} (${skill.level_name})`;
    if (!confirm(`Do You realy want to delete ${skill_name}?`)) {
      toast.error("Operation Declined!");
      return;
    }
    try {
      console.warn({ delete: skill.id });
      await deleteSkill(skill.id);
      toast.success(`${skill_name} Deleted`);
    } catch (err: any) {
      toast.error(err.message);
    }
    // onDeleteSkill?.(skill_id);
  };
  const role = useRole();
  const { deleteSkill } = useSkillsStore();
  return (
    <li key={skill.id} className="p-4 text-white bg-gray-800 rounded shadow">
      {/* Main Container for skill card */}
      <div className="flex">
        {/* Skill Icon */}
        <div className="flex w-1/12">
          <img src={skill.icon_url || "/vite.svg"} alt="skill icon" />
        </div>

        {/* SKill Details */}
        <div className="flex items-center justify-between w-11/12">
        {/* Skill Name and Actions */}
          <div className="flex-1 w-10/12">
            <p className="flex justify-between text-lg font-semibold">
              {skill.name}
            </p>
            <p className="font-semibold">
              <span
                onClick={() => handelDeleteSkill()}
                className="text-red-600 underline hover:cursor-pointer"
              >
                Delete
              </span>
              {role == "Admin" && (
                <Link
                  to={`/edit/${skill.id}`}
                  className="text-blue-400 underline ps-2"
                >
                  Edit
                </Link>
              )}
            </p>
          </div>
          {/*  skill level  */}
          <div className="flex justify-end w-2/12">
            <span className="p-2 text-sm text-center text-green-500 rounded-2xl text-green outline w-100">
             {skill.level_name}
            </span>
          </div>
        </div>
      </div>
    </li>
  );
};

export default SkillCard;
