import type { Skill as SkillType } from "../store/useSkillStore"

type SkillProps = {
    skill : SkillType
}

const SkillCard = ({skill}:SkillProps) => <li  key={skill.id} className="p-4 text-white bg-gray-800 rounded shadow">
    <p className="flex justify-between text-lg font-semibold">{skill.name}     
        <span className="flex items-center space-y-2 text-xs text-green-500 border rounded-2xl text-green outline">Level:{skill.level}</span>
</p>
</li>

export default SkillCard