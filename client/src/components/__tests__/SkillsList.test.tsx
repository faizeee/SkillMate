import {render,screen} from  "@testing-library/react";
import SkillsList from "../SkillsList";
import { Skill } from "../../store/useSkillStore";

describe("SkillsList",()=>{
    it("render skills list mutlti component",()=>{
        const fakeSkills:Skill[] = [
            {name:"php",id:1,level:"Advance"},
            {name:"python",id:2,level:"Beginer"},
            {name:"js",id:2,level:"Intermediate"},
        ];
        render(<SkillsList skills={fakeSkills}/>)
        fakeSkills.forEach(skill =>{
            expect(screen.getByText(new RegExp(skill.name,'i'))).toBeInTheDocument();
            expect(screen.getByText(new RegExp(skill.level,'i'))).toBeInTheDocument();
        })
    });

    it("render no skill message",()=>{
        render(<SkillsList skills={[]}/>)
        expect(screen.getByText(/No Skills/i)).toBeInTheDocument();
    })
});