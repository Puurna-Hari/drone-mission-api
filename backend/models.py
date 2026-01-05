from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class Drone(Base):
    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    model = Column(String)
    status = Column(String, default="available")

    missions = relationship("Mission", back_populates="drone")


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    drone_id = Column(Integer, ForeignKey("drones.id"), nullable=True)
    status = Column(String, default="pending")

    drone = relationship("Drone", back_populates="missions")
    logs = relationship("MissionLog", back_populates="mission")


class MissionLog(Base):
    __tablename__ = "mission_logs"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    message = Column(String, nullable=False)

    mission = relationship("Mission", back_populates="logs")
