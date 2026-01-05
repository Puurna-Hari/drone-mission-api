from fastapi import FastAPI
from backend.routes import drones, missions
from backend.db import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Drone Mission API", version="0.1.0")

app.include_router(drones.router)
app.include_router(missions.router)
