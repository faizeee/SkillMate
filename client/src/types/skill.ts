export type NewSkill = {
  name: string;
  skill_level_id: string | number;
  file?: File
};
// Skill type definition
export type Skill = NewSkill & {
  id: number;
  level_name: string;
  icon_url?:string;
  icon_path?:string;
}; //Composition type or we can directly add name and level attr in Skill

export const SKILL_LEVELS = {
  BEGINNER: 1,
  INTERMEDIATE: 2,
  EXPERT: 3,
} as const;
