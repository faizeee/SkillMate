from fastapi import Form
from models.skill import SkillIn


def get_skill_in(name: str = Form(...), skill_level_id: str = Form(...)) -> SkillIn:
    """Validate the from data using SkillIn model.

    This is a dependency function. It takes all the individual form fields as
    parameters with Form(...) and then creates and
    returns an instance of your SkillIn model.
    FastAPI automatically runs this function and
    validates the data provided in the form.
    """
    return SkillIn(name=name, skill_level_id=skill_level_id)
