import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, vi } from "vitest";
import AddSkillPage from "../../pages/AddSkill";




// 1. Define your mock functions at the top level.
const { toastSuccessMock, toastErrorMock } = vi.hoisted(() => ({
  toastSuccessMock: vi.fn(),
  toastErrorMock: vi.fn(),
}));
const navigateMock = vi.fn();
const addSkillMock = vi.fn(); // Defined here, will set resolved value in beforeEach

// Mock sonner using async/importActual to handle hoisting properly
vi.mock("sonner", async () => {
  const actualSonner = await vi.importActual("sonner");
  return {
    ...actualSonner,
    toast: {
      success: toastSuccessMock,
      error: toastErrorMock,
    },
  };
});

// Mock @tanstack/react-router
vi.mock("@tanstack/react-router", () => ({
  useNavigate: () => navigateMock,
}));

// Mock Zustand Stores (useSkillsStore)
vi.mock("../../store/useSkillStore", () => ({
  useSkillsStore: () => ({
    // Use the top-level addSkillMock here
    addSkill: addSkillMock, // <-- FIXED: Use the top-level mock
    loading: false,
  }),
}));

// Mock Zustand Stores (useSkillLevelStore)
vi.mock("../../store/useSkillLevelStore", () => ({
  useSkillLevelStore: () => ({
    // <-- FIXED: Property name should be 'levels', not 'skillLevels'
    levels: [
      { id: 1, name: "Beginner" },
      { id: 2, name: "Intermediate" },
    ],
    fetchSkillLevels: vi.fn(), // This mock will be called
  }),
}));

describe("AddSkillPage", () => {
  beforeEach(() => {
    // Clear mocks and reset implementations before each test
    vi.clearAllMocks();
    addSkillMock.mockResolvedValue({});
  });

  const getElements = async () => {
    // The select element currently doesn't have a label or aria-label in your component.
    // We'll rely on its display value or a generic role query.
    // screen.getByDisplayValue is generally robust for the default option.
    // For changing its value, you need to target the <select> element itself.
    // A common way to get a select is by its role ('combobox' or 'listbox').
    // If getByRole fails without a name, try finding by other attributes or testId.
    // For a basic <select>, 'combobox' is often the assigned role.
    const skillLevelSelectElement =
      screen.getByRole("combobox") ||
      screen.getByDisplayValue("Select Skill Level");

    return {
      skillNameInput: await screen.findByPlaceholderText("Skill Name"),
      skillLevelSelect: skillLevelSelectElement,
      addBtn: screen.getByText("Add Skill"),
    };
  };

  it("renders form correctly", async () => {
    render(<AddSkillPage />);
    // screen.debug()
    const { skillNameInput, skillLevelSelect, addBtn } = await getElements();

    expect(skillNameInput).toBeInTheDocument();
    expect(skillLevelSelect).toBeInTheDocument();
    expect(addBtn).toBeInTheDocument();
  });

  it("shows the error if name is empty", async () => {
    render(<AddSkillPage />);
    const { addBtn } = await getElements(); // Get elements after render
    fireEvent.click(addBtn);
    await waitFor(() => {
      expect(toastErrorMock).toHaveBeenCalledWith("Name is required");
    });
  });

  it("submits the valid form and navigates", async () => {
    render(<AddSkillPage />);
    // Find form elements
    const { skillNameInput, skillLevelSelect, addBtn } = await getElements(); // Get elements after render

    fireEvent.change(skillNameInput, { target: { value: "React" } });
    // Simulate changing the select value
    fireEvent.change(skillLevelSelect, { target: { value: "1" } }); // Assuming "1" is the ID of "Beginner"

    fireEvent.click(addBtn);

    await waitFor(() => {
      // Assert that addSkill was called with the correct payload
      expect(addSkillMock).toHaveBeenCalledWith({
        name: "React",
        skill_level_id: "1",
      });
      expect(addSkillMock).toHaveBeenCalledTimes(1);
      expect(toastSuccessMock).toHaveBeenCalledWith("New Skill Added");
      expect(navigateMock).toHaveBeenCalledWith({ to: "/skills" });
    });
  });

  it("shows error toast if addSkill fails", async () => {
    addSkillMock.mockRejectedValue(new Error("Server error"));
    render(<AddSkillPage />);
    const { skillNameInput, skillLevelSelect, addBtn } = await getElements();
    fireEvent.change(skillNameInput, { target: { value: "React" } });
    fireEvent.change(skillLevelSelect, { target: { value: "1" } });
    fireEvent.click(addBtn);

    await waitFor(() => {
      expect(toastErrorMock).toHaveBeenCalledWith("Error: Server error"); // Customize message if needed
    });
  });
});
