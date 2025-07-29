import { useAuthStore } from "../store/useAuthStore";
import { useNavigate } from "@tanstack/react-router";

export default function Navbar() {
    const {username,logout} = useAuthStore();
    const navigate = useNavigate()
    const handelLogout = () => {
        logout()
        navigate({to:"/login"})
    }
    return (
        <nav className="flex justify-between p-4 text-white bg-gray-900">
      <h1 className="text-lg font-bold">SkillMate</h1>
      {username && (
        <div className="flex items-center gap-2">
          <span>Hello, {username}</span>
          <button onClick={handelLogout} className="text-red-400 hover:underline hover:cursor-pointer">Logout</button>
        </div>
      )}
    </nav>
    );
}
