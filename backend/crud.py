from sqlalchemy.orm import Session
from backend import models, schemas

def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Mission(
        drone_id=mission.drone_id,
        mission_type=mission.mission_type,
        status=mission.status
    )
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def get_missions(db: Session):
    return db.query(models.Mission).all()


def get_mission(db: Session, mission_id: int):
    return db.query(models.Mission).filter(models.Mission.id == mission_id).first()
