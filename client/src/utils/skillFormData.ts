import type { NewSkill } from "@/types/skill";

export const skillFormData = (skill: NewSkill) => {
  const formData = new FormData();
  formData.append("name", skill.name);
  formData.append("skill_level_id", skill.skill_level_id.toString());
  if (skill.file) {
    formData.append("file", skill.file);
  }
//  for (const [key, val] of formData.entries()) {
//   console.log(key, val);
// }
  return formData;
};
