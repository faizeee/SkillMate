import { render } from "@testing-library/react";
import { useAuthStore } from "@/store/useAuthStore";
import type { User } from "@/types/auth";
import type React from "react";
import { act } from "react";

const createMockUser = (role: string): User => ({
  id: "1",
  username: "TestUser",
  role: {
    id: 1,
    title: role,
    description: `${role} role`,
  },
  role_name: role,
});

export const renderWithAuthRole = (ui: React.ReactElement, role: string) => {
  act(() => {
    useAuthStore.setState({
      token: "mock-test-token",
      user: createMockUser(role),
    });
  });
  return render(ui);
};
