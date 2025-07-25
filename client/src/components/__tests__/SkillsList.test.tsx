import {render,screen} from  "@testing-library/react";
import type { Skill } from "../../store/useSkillStore";
import SkillsList from "../SkillsList";

describe("SkillsList",()=>{
    it("render skills list mutlti component",()=>{
        const fakeSkills:Skill[] = [
            {name:"php",id:1,level:"Advance",skill_level_id:"3"},
            {name:"python",id:2,level:"Beginer",skill_level_id:"1"},
            {name:"js",id:2,level:"Intermediate",skill_level_id:"2"},
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