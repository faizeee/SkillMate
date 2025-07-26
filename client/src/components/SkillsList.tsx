import type { Skill } from "../store/useSkillStore"
import SkillCard from "./SkillCard"

type SkillsListProps = {
    skills : Skill[]
}

export default function SkillsList ({skills}:SkillsListProps){
    if(skills.length == 0 || !skills){
        return <p className="text-red-500"> No Skills</p>
    }

    return (
        <ul className="space-y-2">
            {skills.map((skill,index)=><SkillCard key={index} skill={skill}/>)}
        </ul>
    )

}
