import { useAuthStore } from "@/store/useAuthStore";

export const fetchRequest = async (url: string, options?: RequestInit): Promise<Response> => {
  const token = useAuthStore.getState().token;
  const headers = new Headers(options?.headers);
  // Set default content type if not already provided
  // if (!headers.has("Content-Type")) {
  //   headers.set("Content-Type", "application/json");
  // }
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }
  const updatedOptions: RequestInit = { ...options, headers: headers };
  try {
    const response = await fetch(url, updatedOptions);
    if (response.status === 401) {
      console.log("Authentication token expired or invalid. Logging out.");
      useAuthStore.getState().logout();
    }
    return response;
  } catch (error: any) {
    console.error("Network or fetch request failed:", error);
    throw error;
  }
};
