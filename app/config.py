from sqlmodel import Session, create_engine

USER: str = "postgres"
PASSWORD: str = "demopassword"
DB: str = "postgres"
HOST: str = "localhost"
PORT: str = "5432"


def get_db():
    database_url = f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    engine = create_engine(database_url)
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
