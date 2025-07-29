from sqlmodel import Session, select, delete
from seeders.seed import seed_initial_data
from models.skill import Skill
from models.skill_level import SkillLevel


def test_seed_initial_data_inserted_correctly(test_engine):

    with Session(test_engine) as session:
        session.exec(delete(Skill))
        session.exec(delete(SkillLevel))
        session.commit()

    seed_initial_data(test_engine)

    with Session(test_engine) as session:
        levels = session.exec(select(SkillLevel)).all()
        skills = session.exec(select(Skill)).all()

    assert len(levels) == 3
    assert len(skills) == 6
    assert any(s.name == "Python" for s in skills)


def test_seed_is_idempotent(test_engine):
    with Session(test_engine) as session:
        session.exec(delete(Skill))
        session.exec(delete(SkillLevel))
        session.commit()

    seed_initial_data(test_engine)
    seed_initial_data(test_engine)  # Should not insert again

    with Session(test_engine) as session:
        assert session.exec(select(SkillLevel)).all().__len__() == 3
        assert session.exec(select(Skill)).all().__len__() == 6
