from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend import models
from backend.schemas import DroneCreate, DroneResponse

router = APIRouter(prefix="/drones", tags=["Drones"])


@router.post("/", response_model=DroneResponse)
def create_drone(payload: DroneCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Drone).filter(models.Drone.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Drone with this name already exists")

    drone = models.Drone(name=payload.name, model=payload.model, status="available")
    db.add(drone)
    db.commit()
    db.refresh(drone)
    return drone


@router.get("/", response_model=list[DroneResponse])
def list_drones(db: Session = Depends(get_db)):
    return db.query(models.Drone).all()
