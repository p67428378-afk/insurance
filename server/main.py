
from fastapi import FastAPI
from server.api.v1.endpoints import premium, policies
from server.database import Base, engine

# Create all tables in the database.
# This should be handled by Alembic in a real production environment.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vehicle Insurance Premium Calculator API",
    description="An API to calculate vehicle insurance premiums and manage policies.",
    version="1.0.0"
)

# Include routers
app.include_router(premium.router, prefix="/api/v1/premium", tags=["Premium Calculation"])
app.include_router(policies.router, prefix="/api/v1/policies", tags=["Policies"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vehicle Insurance Premium Calculator API"}
