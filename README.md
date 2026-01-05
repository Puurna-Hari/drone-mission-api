This project is a FastAPI-based backend system to manage drones and their missions efficiently. It allows creating and tracking missions, assigning drones automatically, updating mission statuses, and logging mission events. Designed for real-time operations, it can serve as the foundation for more advanced drone fleet management platforms.

# Drone Mission API

**Version:** 0.1.0  
**Tech Stack:** FastAPI, SQLAlchemy, SQLite, Pydantic, Python 3.12  

A backend API to manage drones, missions, and mission logs. Supports automatic drone assignment, mission status updates, and logs tracking.

---

## **Table of Contents**

1. [Project Setup](#project-setup)  
2. [Run the Server](#run-the-server)  
3. [API Endpoints](#api-endpoints)  
4. [Testing Order](#testing-order)  
5. [Future Enhancements](#future-enhancements)  

---

## **Project Setup**

1. Clone the repository:

2. flyt_internship1/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       ├── drones.py
│       ├── missions.py
│
├── venv/                 # virtual environment (usually not pushed)
├── requirements.txt
├── README.md
└── .gitignore


```bash
git clone https://github.com/USERNAME/drone-mission-api.git
cd drone-mission-api
