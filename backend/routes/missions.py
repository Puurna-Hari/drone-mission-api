from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import get_db
from backend import models
from backend.schemas import (
    MissionCreate,
    MissionResponse,
    MissionStatusUpdate,
    MissionLogCreate,
    MissionLogResponse
)

router = APIRouter(prefix="/missions", tags=["Missions"])


# --- Missions ---
@router.post("/", response_model=MissionResponse)
def create_mission(payload: MissionCreate, db: Session = Depends(get_db)):
    mission = models.Mission(
        name=payload.name,
        description=payload.description,
        drone_id=payload.drone_id,
        status="pending"
    )
    db.add(mission)
    db.commit()
    db.refresh(mission)
    return mission


@router.get("/", response_model=list[MissionResponse])
def list_missions(db: Session = Depends(get_db)):
    return db.query(models.Mission).all()


@router.patch("/{mission_id}/status", response_model=MissionResponse)
def update_mission_status(
    mission_id: int,
    payload: MissionStatusUpdate,
    db: Session = Depends(get_db)
):
    mission = db.query(models.Mission).filter(models.Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")

    allowed_statuses = ["pending", "running", "completed", "failed"]
    if payload.status not in allowed_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")

    mission.status = payload.status
    db.commit()
    db.refresh(mission)
    return mission


# --- Mission Logs ---
@router.post("/logs/", response_model=MissionLogResponse)
def create_mission_log(payload: MissionLogCreate, db: Session = Depends(get_db)):
    mission = db.query(models.Mission).filter(models.Mission.id == payload.mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")

    log = models.MissionLog(mission_id=payload.mission_id, message=payload.message)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


@router.get("/{mission_id}/logs", response_model=list[MissionLogResponse])
def list_mission_logs(mission_id: int, db: Session = Depends(get_db)):
    logs = db.query(models.MissionLog).filter(models.MissionLog.mission_id == mission_id).all()
    return logs
