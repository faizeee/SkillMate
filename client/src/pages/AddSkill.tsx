import { useEffect, useState } from "react";
import { useSkillsStore } from "../store/useSkillStore";
import { useNavigate } from "@tanstack/react-router";
import { toast } from "sonner";
import { useSkillLevelStore } from "../store/useSkillLevelStore";

export default function AddSkillPage() {
  const { levels: skillLevels, fetchSkillLevels } = useSkillLevelStore();
  const [name, setName] = useState("");
  const [skill_level_id, setSkillLevelId] = useState("");
  const { addSkill, loading } = useSkillsStore();
  const navigate = useNavigate();
  useEffect(() => {
    fetchSkillLevels();
  }, []);
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Frontend validation
    if (!name.trim()) {
      toast.error("Name is required");
      return;
    }
    await addSkill({ name, skill_level_id })
      .then(() => toast.success("New Skill Added"))
      .then(() => {
        console.info("redirecting to skills page");
        // ✅ Only navigate if no error
        navigate({ to: "/skills" });
      })
      .catch((err) => toast.error(`${err || "Something went wrong"}`));
  };

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold text-gray-500">➕ Add a New Skill</h1>
      <form onSubmit={handleSubmit} className="max-w-md space-y-4">
        <input
          type="text"
          placeholder="Skill Name"
          className="w-full px-4 py-2 text-white bg-gray-800 rounded"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <select
          value={skill_level_id}
          onChange={(e) => setSkillLevelId(e.target.value)}
          className="w-full px-4 py-2 text-white bg-gray-800 rounded"
        >
          <option value="">Select Skill Level</option>
          {skillLevels.map((skillLevel, index) => (
            <option key={index} value={skillLevel.id}>
              {skillLevel.name}
            </option>
          ))}
        </select>

        <button
          type="submit"
          className="px-4 py-2 text-white bg-green-600 rounded hover:bg-green-700"
          disabled={loading}
        >
          {/*!name || !skill_level_id ||*/}
          Add Skill
        </button>
      </form>
    </div>
  );
}
