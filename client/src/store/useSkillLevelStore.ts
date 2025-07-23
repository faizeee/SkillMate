import { create } from "zustand";
import { fetchWrapper } from "../utils/fetchWrapper";
import { toast } from "sonner";

export type SkillLevel = {
    id:number;
    name:string;
    description:string;
}

type SkillLevelState = {
    levels: SkillLevel[];
    loading:boolean;
    fetchSkillLevels: () => Promise<void>;
}

const BASE_URL = import.meta.env.VITE_API_URL;

export const useSkillLevelStore = create<SkillLevelState>((set)=>({
    levels:[],
    loading:false,
    fetchSkillLevels: async ()=>{
        await fetchWrapper(`${BASE_URL}/skills/levels`,{
            onStart:()=>set({loading:true}),
            onSuccess:(data)=>set({levels:data}),
            onError:(err)=>toast(err),
            onFinish:()=>set({loading:false})
        })
    }
}));

