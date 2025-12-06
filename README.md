# DroneKit–Gazebo UAV Simulation (ArduCopter / SITL)

> **Domain:** UAV Simulation / Telemetry / Autopilot  
> **Level:** Prototype (Student R&D)  
> **Purpose:** Establish a minimal UAV simulation environment using DroneKit, Gazebo and ArduPilot SITL for basic flight control experimentation.

---

## 1. Background & Objective
Modern UAV systems rely on safe autonomous flight, reliable telemetry and accurate sensor simulation before real flight testing.  
This project sets up a **virtual drone environment** using DroneKit (Python), Gazebo and ArduPilot’s SITL (Software In The Loop) to experiment with basic flight commands, mode changes and telemetry flow.

The objective is not to create a full mission controller, but to build a **working foundation** for future experiments in autonomous control and UAV decision logic.

---

## 2. Technologies
- Python 3.10+
- DroneKit
- MAVProxy
- ArduPilot SITL (ArduCopter)
- Gazebo 11
- Virtual Environment (.venv)

---

## 3. Project Structure
dronekit_gazebo_project/
│
├── main.py
├── requirements.txt
├── .venv/
└── README.md

---
## 4. Installation & Run

### Create virtual environment
```bash
python -m venv .venv

