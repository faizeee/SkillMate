import { create } from "zustand";
import { fetchWrapper } from "../utils/fetchWrapper";
// Skill type definition
export type Skill = {
  id: number;
  name: string;
  level: number;
};

type SkillState = {
  skills: Skill[];
  loading: boolean;
  error: string | null;
  fetchSkills: () => Promise<void>;
};

// Zustand store for global state

export const useSkillsStore = create<SkillState>((set) => ({
  skills: [],
  loading: false,
  error: null,
  fetchSkills: async () => {
    await fetchWrapper("http://localhost:8000/api/skills", {
      onStart: () => set({ loading: true, error: null }),
      onSuccess: (data) => set({ skills: data }),
      onError: (err) => set({ error: err }),
      onFinish: () => set({ loading: false }),
    });
  },
}));
