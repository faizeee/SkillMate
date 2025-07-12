import { create } from "zustand";
import { fetchWrapper } from "../utils/fetchWrapper";
export type NewSkill = {
  name: string;
  level: string;
};

// Skill type definition
export type Skill = {id: number} & NewSkill //Composition type or we can directly add name and level attr in Skill  

type SkillState = {
  skills: Skill[];
  loading: boolean;
  error: string | null;
  fetchSkills: () => Promise<void>;
  addSkill:(skill:NewSkill) => Promise<void>;
  
};
const BASE_URL = import.meta.env.VITE_API_URL
// Zustand store for global state
export const useSkillsStore = create<SkillState>((set) => ({
  skills: [],
  loading: false,
  error: null,
  fetchSkills: async () => {
    await fetchWrapper(`${BASE_URL}/api/skills`, {
      onStart: () => set({ loading: true, error: null }),
      onSuccess: (data) => set({ skills: data }),
      onError: (err) => set({ error: err }),
      onFinish: () => set({ loading: false }),
    });
  },

  addSkill: async (skill) => {
    await fetchWrapper(`${BASE_URL}/api/skills`,{
    method: "POST",
    body: JSON.stringify(skill),
    headers: { "Content-Type": "application/json" },
    onStart:()=>set({loading:true,error:null}),
    onSuccess:(newSkill)=>set((state)=>({skills:[...state.skills,newSkill]})),
    onError:(error)=>set({error:error}),
    onFinish:()=>set({loading:false})
  })
  }
}));
