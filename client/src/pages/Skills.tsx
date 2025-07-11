import { useEffect } from "react";
import { useSkillsStore } from "@/store/useSkillStore";
import type { Skill } from "../store/useSkillStore";
export default function SkillsPage() {
  const {skills, loading, error, fetchSkills} = useSkillsStore();
  useEffect(()=>{
    fetchSkills();
  },[]);
  
  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold text-white">🧠 Skill List</h1>
      {loading &&  <p className="text-yellow-400">Loading skills...</p>}
      {error &&  <p className="text-red-500">{error}</p>}
      {skills.length === 0 && !loading && <p className="text-red-500">No Skills</p>} 
       <ul className="space-y-2">
        <li className="text-lg font-bold">This is skills UL</li>
        {skills.map((skill:Skill)=>{
            return (<li key={skill.id} className="p-4 text-white bg-gray-800 rounded shadow">
              <p className="text-lg font-semibold">{skill.name}</p>
              <p className="text-sm text-gray-400">Level:{skill.level}</p>
            </li>)
          })}
       </ul>
      
      </div>
  );
}
