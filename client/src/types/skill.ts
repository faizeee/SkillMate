export type NewSkill = {
  name: string;
  skill_level_id: string | number;
};
// Skill type definition
export type Skill = { id: number; level_name: string } & NewSkill; //Composition type or we can directly add name and level attr in Skill

export const SKILL_LEVELS = {
    BEGINNER: 1,
    INTERMEDIATE: 2,
    EXPERT: 3,
} as const;
