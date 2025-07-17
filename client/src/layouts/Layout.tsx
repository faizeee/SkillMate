import { Outlet, Link} from "@tanstack/react-router";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
// import { useAuthStore } from "../store/useAuthStore";
export default function Layout() {
  
  // const is_loggedin = useAuthStore(s => s.is_loggedin())
  // if(!is_loggedin) return <Navigate to='/login'/>

  return (
    <div className="min-h-screen">
   {/* Navbar */}
      <Navbar/>
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <Sidebar/>
      {/* Main Content */}
      <main className="flex-1 p-6 bg-gray-50">
        <Outlet />
      </main>
    </div>
    </div>
  );
}
