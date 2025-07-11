import { Outlet, Link } from "@tanstack/react-router";
export default function Layout() {
  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <aside className="w-64 p-4 text-white bg-primary">
        <h1 className="mb-6 text-2xl font-bold">SkillMate</h1>
        <nav className="flex flex-col space-y-2">
          <Link to="/" className="[&.active]:font-bold">
            Home
          </Link>
          <Link to="/skills" className="[&.active]:font-bold">
            Skills
          </Link>
          <Link to="/profile" className="[&.active]:font-bold">
            Profile
          </Link>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6">
        <Outlet />
      </main>
    </div>
  );
}
