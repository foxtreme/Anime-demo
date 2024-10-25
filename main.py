from fastapi import FastAPI, Depends
from sqlmodel import Session, text
from app.routers import anime_router
from app.config import get_db

app = FastAPI()


@app.get("/health-check")
def read_root(db: Session = Depends(get_db)):
    try:
        db.exec(text("Select 1"))
        return {
            "status": "up",
            "database": "up",
        }
    except Exception as e:
        return {
            "status": "down",
            "database": "down",
            "error": str(e),
        }


app.include_router(anime_router.router)
