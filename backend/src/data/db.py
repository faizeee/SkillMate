from .fake_skills import fake_skills
from sqlmodel import Session, SQLModel, create_engine
from typing import Generator

DATABASE_URL  = "sqlite:///backend/skillmate.db"
engine  = create_engine(DATABASE_URL,echo=True)

""" Explanation: This defines a Python generator function.

with Session(engine) as session:: This is a context manager. It ensures that a database session is properly opened and, most importantly, properly closed (or rolled back if an error occurs).

    Session(engine): Creates a new database session connected to the engine.

    as session: Assigns the created session object to the variable session.

yield session: This is the core of a generator function. Instead of returning a value and exiting, yield pauses the function's execution, returns the session object, and remembers its state. When the caller is done with the session (e.g., when the with block in the caller finishes), execution resumes right after the yield, and the session is automatically closed by the with statement.

Purpose: This function is designed to be used as a dependency in web frameworks (like FastAPI) or other parts of your application where you need a database session. It provides a clean and safe way to get a session, use it, and ensure it's closed, preventing resource leaks. """

def get_session() -> Generator[Session, None, None]:
    """
    Dependency to provide a database session.
    It ensures the session is properly closed after the request.
    """
    with Session(engine) as session:
        # print(f"--- DEBUG: Session object created in get_session: {type(session)}, ID: {id(session)} ---")
        yield session



"""     Explanation: This defines a function to initialize your database schema.

        SQLModel.metadata.create_all(engine): This is the crucial line for setting up your database tables.

            SQLModel.metadata: This object holds all the metadata about your SQLModel classes (i.e., the table definitions you've created by inheriting from SQLModel).

            create_all(engine): This method inspects all the tables defined in SQLModel.metadata and issues CREATE TABLE statements to the database connected via the engine. If the tables already exist, it typically does nothing (it won't update existing tables if their schema changes; for that, you'd use a migration tool like Alembic).

        Purpose: You would call this function once when your application starts up for the first time, or during a setup script, to create all the necessary tables in your skillmate.db file.

 """
def init_db() ->None :
    SQLModel.metadata.create_all(engine)