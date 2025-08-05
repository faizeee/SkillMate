import { create } from "zustand";
import type { LoginCredentials, User, AuthResponse } from "../types/auth";
interface AuthState {
  token: string | null;
  user: User | null;
  setAuth: (res: AuthResponse) => void;
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => void;
  is_loggedin: () => Boolean;
  username: () => string | null;
}
const BASE_URL = import.meta.env.VITE_API_URL;

// Helper to safely get and parse the user from localStorage
const getInitialUserState = (): User | null => {
  const userStr = localStorage.getItem("user");
  return userStr ? JSON.parse(userStr) : null;
};

export const useAuthStore = create<AuthState>((set, get) => ({
  token: localStorage.getItem("token"),
  user: getInitialUserState(),
  is_loggedin: () => !!get().token,
  username: () => get().user?.username ?? null,
  setAuth: (res: AuthResponse) => {
    localStorage.setItem("token", res.access_token);
    localStorage.setItem("user", JSON.stringify(res.user));
    set({ user: res.user, token: res.access_token });
  },
  logout: () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    set({ token: null, user: null });
  },
  login: async (credentials: LoginCredentials) => {
    try {
      const res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials),
      });
      if (!res.ok) throw new Error("Invalid credentials");
      const data = await res.json();
      get().setAuth(data);
    } catch (err) {
      console.error("Login failed", err);
      throw err;
    }
  },
}));
