import { Navigate, Outlet } from '@tanstack/react-router'
import { useAuthStore } from '@/store/useAuthStore'

export default function AuthLayout() {
  const token = useAuthStore((s) => s.token)

  if (!token) return <Navigate to="/login" />

  // Renders all child routes
  return <Outlet />
}