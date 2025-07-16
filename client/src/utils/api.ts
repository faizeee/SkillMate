import type { LoginCredentials } from "../types/auth";

export async function loginUser(credentials:LoginCredentials) {
     const res = await fetch("http://localhost:8000/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });

  if (!res.ok) throw new Error("Invalid credentials");
  return res.json(); // { access_token: string, token_type: "bearer" }
}