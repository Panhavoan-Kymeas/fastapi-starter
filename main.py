from fastapi import FastAPI
from core.database import Base, engine
from apps.users.routes import router as users_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Starter!"}