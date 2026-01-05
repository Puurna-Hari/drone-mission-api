from pydantic import BaseModel
from typing import Optional


# --- Drone Schemas ---
class DroneCreate(BaseModel):
    name: str
    model: str


class DroneResponse(BaseModel):
    id: int
    name: str
    model: str
    status: str

    class Config:
        from_attributes = True


# --- Mission Schemas ---
class MissionCreate(BaseModel):
    name: str
    description: Optional[str] = None
    drone_id: Optional[int] = None


class MissionResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    drone_id: Optional[int]
    status: str

    class Config:
        from_attributes = True


class MissionStatusUpdate(BaseModel):
    status: str


# --- Mission Log Schemas ---
class MissionLogCreate(BaseModel):
    mission_id: int
    message: str


class MissionLogResponse(BaseModel):
    id: int
    mission_id: int
    message: str

    class Config:
        from_attributes = True
