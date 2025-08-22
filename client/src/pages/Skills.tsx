import { useEffect } from "react";
import { useSkillsStore } from "@/store/useSkillStore";
import SkillsList from "@/components/SkillsList";
import { Link } from "@tanstack/react-router";

export default function SkillsPage() {
  const {skills, loading, error, fetchSkills} = useSkillsStore();

  useEffect(()=>{
    // Only fetch skills if the array is empty
    if(skills.length === 0){
      fetchSkills();
    }
  },[skills.length,fetchSkills]);

  return (
    <div className="p-6 space-y-4">
      <h1 className="flex justify-between text-2xl font-bold text-gray-700">🧠 Skill List
        <Link to='/add'>+ Add New Skill</Link>
      </h1>
      {loading &&  <p className="text-yellow-400">Loading skills...</p>}
      {error &&  <p className="text-red-500">{error}</p>}
      <SkillsList skills={skills}/>
      {/* {skills.length === 0 && !loading && <p className="text-red-500">No Skills</p>}
       <ul className="space-y-2">
        <li className="text-lg font-bold">This is skills UL</li>
        {skills.map((skill:Skill)=>{
            return (<li key={skill.id} className="p-4 text-white bg-gray-800 rounded shadow">
              <p className="text-lg font-semibold">{skill.name}</p>
              <p className="text-sm text-gray-400">Level:{skill.level}</p>
            </li>)
          })}
       </ul> */}

      </div>
  );
}
