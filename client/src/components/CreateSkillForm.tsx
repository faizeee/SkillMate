import { useSkillLevelStore } from "@/store/useSkillLevelStore";
import { SKILL_LEVELS, type NewSkill } from "@/types/skill";
import { useEffect, useMemo, useState, type ChangeEvent } from "react";
import { toast } from "sonner";

interface CreateSkillFormProps {
  editSkill?: NewSkill;
  loading?: boolean;
  onSubmit: (FormData: NewSkill) => void;
}

export default function CreateSkillForm({
  editSkill,
  loading = false,
  onSubmit,
}: CreateSkillFormProps) {
  const [formData, setFormData] = useState<NewSkill>({
    name: editSkill?.name || "",
    skill_level_id: editSkill?.skill_level_id || SKILL_LEVELS.BEGINNER,
  });

  const handleInputChange = (e: ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    console.info({ name, value });

    setFormData(prevData => ({
      ...prevData,
      [name]: value,
    }));
  };

  // levels: skillLevels is a special kind of destructuring called renaming. It gets the property named levels from the object and assigns its value to a new local variable named skillLevels. This is useful for avoiding naming conflicts or simply making the variable name more descriptive in the local scope.
  const { levels: skillLevels, fetchSkillLevels } = useSkillLevelStore();

  //computed or we can do "const title = defaultValues ? 'Edit Skill' : 'Add Skill'";
  const title = useMemo(() => {
    const pre_fix = editSkill ? `Edit  ${editSkill.name}` : "Add";
    return `${pre_fix} Skill`;
  }, [editSkill]);

  // this mounted function
  useEffect(() => {
    fetchSkillLevels();
  }, []);
  const handelSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Frontend validation
    if (!formData.name.trim()) {
      toast.error("Name is required");
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold text-gray-500">{title}</h1>
      <form onSubmit={handelSubmit} className="max-w-md space-y-4">
        <input
          type="text"
          name="name"
          placeholder="Skill Name"
          className="w-full px-4 py-2 text-white bg-gray-800 rounded"
          value={formData.name}
          onChange={handleInputChange}
        />

        <select
        name="skill_level_id"
          value={formData.skill_level_id}
          onChange={handleInputChange}
          className="w-full px-4 py-2 text-white bg-gray-800 rounded"
        >
          {skillLevels.map((level) => (
            <option value={level.id} key={level.id}>
              {level.name}
            </option>
          ))}
        </select>

        <button
          type="submit"
          className="px-4 py-2 text-white bg-green-600 rounded hover:bg-green-700"
          disabled={loading}
        >
          {/*!name || !skill_level_id ||*/}
          Submit
        </button>
      </form>
    </div>
  );
}
