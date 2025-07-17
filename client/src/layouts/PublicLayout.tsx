import { Navigate, Outlet } from '@tanstack/react-router'
import { useAuthStore } from '@/store/useAuthStore'

export default function PublicLayout() {
  const is_loggedin = useAuthStore(s => s.is_loggedin())
  if(is_loggedin) return <Navigate to='/'/>
  // Renders all child routes
  return (
    <div className="flex min-h-screen">
       {/* Main Content */}
      <main className="flex-1 p-6 bg-gray-50">
        <Outlet />
      </main>
    </div>
    
  )
}