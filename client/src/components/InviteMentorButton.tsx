import { useRole } from "@/hooks/useRole";

export default function InviteMentorButton() {
  const role = useRole();
  if (role != "Admin") return null;
  return (
    <button className="px-4 py-2 text-white bg-blue-600 rounded">
      Invite Mentor
    </button>
  );
}
