import { useAuthStore } from "@/store/useAuthStore";
import { useEffect } from "react";
import { useNavigate } from "@tanstack/react-router";

export const useAuthRedirect = (login_url: string = "/login") => {
  const token = useAuthStore((state) => state.token);
  const navigate = useNavigate();
  useEffect(() => {
    if (!!token) return;
    console.info(`logged out redirecting to ${login_url}!`);
    navigate({ to: login_url });
  }, [token, login_url, navigate]);
};
