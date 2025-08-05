import InviteMentorButton from "@/components/InviteMentorButton";

export default function HomePage() {
  return (
    <div className="space-y-4">
      <h2 className="text-xl font-semibold">Welcome to SkillMate 👋</h2>
      <h1 className="text-4xl font-bold text-green-500">
        Tailwind 4 is Working ✅
      </h1>
      <div className="p-6 text-white bg-red-500 rounded-lg">
        This is Tailwind 🔥
      </div>
      <InviteMentorButton />
    </div>
  );
}
