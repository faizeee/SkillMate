import { Link } from "@tanstack/react-router"
export default function Sidebar (){
    return (
        <aside className="w-64 p-4 text-blue-400 bg-gray-300">
<nav className="flex flex-col space-y-2">
          <Link to="/" className="[&.active]:font-bold">
            Home
          </Link>
          <Link to="/add" className="[&.active]:font-bold">
            Add New Skills
          </Link>
          <Link to="/skills" className="[&.active]:font-bold">
            Skills
          </Link>
          <Link to="/profile" className="[&.active]:font-bold">
            Profile
          </Link>
        </nav>
        </aside>
    )
}