import { useRole } from "@/hooks/useRole"
import { useSkillsStore } from "@/store/useSkillStore"
import type { Skill as SkillType } from "@/types/skill"
import { Link } from "@tanstack/react-router"
import { toast } from "sonner"

type SkillProps = {
    skill : SkillType,
    // onDeleteSkill ?: (skill_id: number | string)=>void
}

const SkillCard = ({skill}:SkillProps) => {
    const handelDeleteSkill  =  async () => {
        const skill_name = `${skill.name} (${skill.level_name})`;
        if(!confirm(`Do You realy want to delete ${skill_name}?`)){
            toast.error("Operation Declined!")
            return;
        }
        try{
            console.warn({delete:skill.id})
            await deleteSkill(skill.id);
            toast.success(`${skill_name} Deleted`)
       }catch(err:any){
        toast.error(err.message)
       }
        // onDeleteSkill?.(skill_id);
    }
    const role = useRole()
    const {deleteSkill} = useSkillsStore()
    return (
        <li  key={skill.id} className="p-4 text-white bg-gray-800 rounded shadow">
    <p className="flex justify-between text-lg font-semibold">{skill.name}
        <span className="flex items-center space-y-2 text-xs text-green-500 border rounded-2xl text-green outline">
            Level:{skill.level_name}
        </span>
</p>
<p className="font-semibold">
    <span onClick={()=>handelDeleteSkill()} className="text-red-600 underline hover:cursor-pointer">Delete</span>
    {role == "Admin" && (<Link to = {`/edit/${skill.id}`} className="text-blue-400 underline ps-2" > Edit </Link>)}
</p>
</li>
    );
}

export default SkillCard
