
from fastapi import FastAPI
from server.app.api.v1.router import api_router
from server.app.db.session import engine
from server.app.models.policy import Base

app = FastAPI(title="Vehicle Insurance Premium Calculator")

@app.on_event("startup")
def on_startup():
    # This is for SQLite. For PostgreSQL, you would use Alembic migrations.
    if "sqlite" in str(engine.url):
        Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vehicle Insurance Premium Calculator API"}
