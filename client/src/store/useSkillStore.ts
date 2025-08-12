import { create } from "zustand";
import { fetchWrapper } from "../utils/fetchWrapper";
import { toast } from "sonner";
import type { Skill, NewSkill } from "@/types/skill";
import { fetchRequest } from "@/utils/fetchRequest";
import { handleApiError } from "@/utils/apiErrorHandler";

type SkillState = {
  skills: Skill[];
  loading: boolean;
  error: string | null;
  fetchSkills: () => Promise<void>;
  addSkill: (skill: NewSkill) => Promise<void>;
  updateSkill: (skill: NewSkill, skill_id: number | string) => Promise<void>;
  getSkill: (skill_id: number | string) => Skill | null;
  deleteSkill: (skill_id: number | string) => Promise<void>;
};
const BASE_URL = import.meta.env.VITE_API_URL;
// Zustand store for global state
export const useSkillsStore = create<SkillState>((set, get) => ({
  skills: [],
  loading: false,
  error: null,
  fetchSkills: async () => {
    await fetchWrapper(`${BASE_URL}/skills`, {
      onStart: () => set({ loading: true, error: null }),
      onSuccess: (data) => set({ skills: data }),
      onError: (err) => set({ error: err }),
      onFinish: () => set({ loading: false }),
    });
  },
  getSkill: (skill_id: number | string) => {
    return get().skills.find(skill => skill.id == skill_id) || null
  },

  // getSkill: async (skill_id: number | string) => {
  //   try {
  //     const response = await fetchRequest(`${BASE_URL}/skills/${skill_id}`);
  //     const skill = await response.json();
  //     if (!response.ok) {
  //       throw new Error("Failed to fetch skill");
  //     }
  //     console.log(skill);
  //     return skill;
  //   } catch (err) {
  //     set({ error: (err as Error).message });
  //     console.error(err);
  //     return null;
  //   }
  // },

  deleteSkill: async (skill_id: number | string) => {
    try {
      const skillToDelete = get().getSkill(skill_id);
      if(!skillToDelete) {
        toast.error("Invalid Skill!")
        return;
      }

      if(!confirm(`Do You realy want to delete ${skillToDelete.name} (${skillToDelete.level_name})?`)){
        toast.error("Operation Declined!")
        return;
      }

      const response = await fetchRequest(`${BASE_URL}/skills/${skill_id}`, {
        method: "delete",
      });
      if (!response.ok) {
        throw new Error("Something went wrong!");
      }
      console.log({skillToDelete})
      set((state) => ({skills: state.skills.filter((s)=>s.id == skill_id)}))
      return;
    } catch (err: any) {
      console.log(err.message);
      throw new Error(err.message);
    }
  },
  addSkill: async (skill) => {
    try {
      const response = await fetchRequest (`${BASE_URL}/skills`,{
        method: "POST",
        body: JSON.stringify(skill)
      });
      if (!response.ok) {
        await handleApiError(response);
      }
      const createdSkill = await response.json();
      console.log({createdSkill})
      set((state) => ({skills:[...state.skills,createdSkill]}))
      toast.success("Skill added Successfully");
      return;
    } catch (err: any) {
      set({ error: err.message });
      throw new Error(err.message);
    } finally {
      set({ loading: false });
    }
  },

  updateSkill: async (skill: NewSkill, skill_id: number | string) => {
    try {
      const response = await fetchRequest(`${BASE_URL}/skills/${skill_id}`, {
        method: "patch",
        body: JSON.stringify(skill),
      });

      if (!response.ok) {
        await handleApiError(response);
      }
      const updatedSkill = await response.json()
      console.log({updatedSkill})
      // Use the 'set' function to update the state directly
      set((state)=>({skills: state.skills.map((s)=>s.id == skill_id ? updatedSkill : s)}))
      return;
    } catch (err: any) {
      set({ error: err.message });
      throw err;
    }
  },
}));
