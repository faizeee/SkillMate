import { useAuthStore } from "@/store/useAuthStore";

export default function Dashboard() {
  const username = useAuthStore((state) => state.username());
  return <p>Welcome to {username ?? "Admin"}</p>;
}
