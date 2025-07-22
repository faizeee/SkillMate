import {render,screen} from "@testing-library/react";
import SkillCard from "../SkillCard";

describe('SkillCard',()=>{
    const fakeSkill = {
      id: 1,
      name: 'React',
      level: 'Intermediate'
    };
    it("renders skill name and level",()=>{
        render(<SkillCard skill={fakeSkill} />);
        expect(screen.getByText(/react/i)).toBeInTheDocument();
        expect(screen.getByText(/intermediate/i)).toBeInTheDocument();
    });
});