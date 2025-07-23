import { create } from "zustand";
import type { LoginCredentials } from "../types/auth";

interface AuthState {
    token: string | null;
    username: string | null;
    id: string | null;
    setAuth : (token:string , username:string) => void;
    login: (credentials:LoginCredentials) => Promise<void>;
    logout : () => void;
    is_loggedin : ()=> Boolean
}
const BASE_URL = import.meta.env.VITE_API_URL

export const useAuthStore = create<AuthState>((set,get)=>({
    token:localStorage.getItem("token"),
    username :localStorage.getItem('username'),
    id : localStorage.getItem('id'),
    is_loggedin : () => !!get().token,
    setAuth: (token,username) => {
        localStorage.setItem("token",token)
        localStorage.setItem("username",username)
        // localStorage.setItem("id",id)
        set({ username: username, token: token })

    },
    logout : () => {
        localStorage.removeItem("token")
        localStorage.removeItem("username")
        // localStorage.removeItem("id")
        set({token:null,username:null,id:null})
    },
    login : async (credentials:LoginCredentials) => {
        try {
      const res = await fetch(`${BASE_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      })
      if (!res.ok) throw new Error('Invalid credentials')
      const data = await res.json()
      get().setAuth(data.access_token,credentials.username)
    } catch (err) {
      console.error('Login failed', err)
      throw err // let the UI handle it
    }
      }
}))