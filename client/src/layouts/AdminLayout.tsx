import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import AppToaster from "@/components/ui/AppToaster";
import { Outlet } from "@tanstack/react-router";

export default function AdminLayout() {
  return (
    <div className="min-h-screen">
      {/* Navbar */}
      <Navbar />
      <div className="flex min-h-screen">
        {/* Sidebar */}
        <Sidebar />
        {/* Main Content */}
        <main className="flex-1 p-6 bg-gray-50">
          <h1 className="text-2xl">Admin Dashboard</h1>
          <Outlet />
          <AppToaster />
        </main>
      </div>
    </div>
  );
}
