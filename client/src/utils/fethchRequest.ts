import { useAuthStore } from "@/store/useAuthStore";

export const fetchRequest = (url: string, options: RequestInit) => {
  const token = useAuthStore.getState().token;
  const headers = new Headers(options.headers);
  // Set default content type if not already provided
  if (!headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }
  const updatedOptions: RequestInit = { ...options, headers: headers };

  return fetch(url, updatedOptions);
};
