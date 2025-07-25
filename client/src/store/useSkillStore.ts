import { create } from "zustand";
import { fetchWrapper } from "../utils/fetchWrapper";
import { useAuthStore } from "./useAuthStore";
import { toast } from "sonner";


export type NewSkill = {
  name: string;
  skill_level_id:string;
};
// Skill type definition
export type Skill = {id: number,  level: string} & NewSkill //Composition type or we can directly add name and level attr in Skill  

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
    await fetchWrapper(`${BASE_URL}/skills`, {
      onStart: () => set({ loading: true, error: null }),
      onSuccess: (data) => set({ skills: data }),
      onError: (err) => set({ error: err }),
      onFinish: () => set({ loading: false }),
    });
  },

  addSkill: async (skill) => {
    try{
const token = useAuthStore.getState().token;
   const response =  await fetch(`${BASE_URL}/skills`,{
    method: "POST",
    body: JSON.stringify(skill),
    headers: { 
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}` 
    },
    });
    if(!response.ok){
      const err_data = await response.json()
      let err_message = "Something went wrong";

if (typeof err_data.detail === "string") {
  err_message = err_data.detail;
} else if (Array.isArray(err_data.detail)) {
  err_message = err_data.detail.map((e: any) => e.msg).join(", ");
} else if (typeof err_data.detail === "object" && err_data.detail.message) {
  err_message = err_data.detail.message;
}
      set({error:err_message});
      console.error(err_message)
      throw new Error(response.status === 409 ? "Skill Already Exits" :  err_message);
    }
    toast.success("Skill added Successfully");
    return;
    }catch(err:any){
           set({error:err.message});
           throw new Error(err.message)
    } finally {
      set({loading:false})
    }
    
  //   await fetchWrapper(`${BASE_URL}/skills`,{
  //   method: "POST",
  //   body: JSON.stringify(skill),
  //   headers: { "Content-Type": "application/json" },
  //   onStart:()=>set({loading:true,error:null}),
  //   onSuccess:(newSkill)=>set((state)=>({skills:[...state.skills,newSkill]})),
  //   onError:(err)=>{
  //     set({error:err})
  //     throw new Error(err)
  //   },
  //   onFinish:()=>set({loading:false})
  // })
  }
}));
