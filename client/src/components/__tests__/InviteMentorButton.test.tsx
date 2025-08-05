import { screen } from "@testing-library/react";
import { renderWithAuthRole } from "./utils/test-utils";
import { useAuthStore } from "@/store/useAuthStore";
import InviteMentorButton from "../InviteMentorButton";

describe("InviteMentorButton", () => {
  afterEach(() => {
    useAuthStore.setState({ token: null, user: null });
  });

  it("should render the invite button for admin", () => {
    renderWithAuthRole(<InviteMentorButton />, "admin");
    expect(screen.getByText("Invite Mentor")).toBeInTheDocument();
  });

  it("should not render the invite button for user", () => {
    renderWithAuthRole(<InviteMentorButton />, "user");
    expect(screen.queryByText("Invite Mentor")).not.toBeInTheDocument();
  });
});
