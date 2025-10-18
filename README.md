🧠 Overview

This project simulates an autonomous drone mission in the Gazebo simulation environment using DroneKit-Python and ArduPilot SITL.
The goal was to connect to a simulated drone, switch to GUIDED mode, take off, and move from one point to another automatically.

This work was prepared as part of the KÜ OAT Club Application Assignment to demonstrate DroneKit–Gazebo integration and autonomous flight logic.

⚙️ Technologies Used

Python 3.10+

DroneKit-Python

ArduPilot SITL

MAVProxy

Gazebo

VS Code (development environment)

Virtual Environment (.venv) for dependency management

🪜 Setup & Installation

Clone this repository

git clone https://github.com/MeldaYuceee/dronekit_gazebo_project.git
cd dronekit_gazebo_project


Create and activate virtual environment

python -m venv .venv
.venv\Scripts\activate    # Windows
# or
source .venv/bin/activate # macOS / Linux


Install dependencies

pip install dronekit dronekit-sitl mavproxy


Launch SITL (Software In The Loop)

sim_vehicle.py -v ArduCopter -L KSFO --console --map


Run the mission script

python main.py

🧩 main.py Summary

The script connects to the simulated drone, waits for GPS lock, switches to GUIDED mode, and executes a simple waypoint mission.

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

print("Arming drone...")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
time.sleep(3)

print("Taking off...")
vehicle.simple_takeoff(10)

target = LocationGlobalRelative(37.874, -122.302, 10)
print("Going to target waypoint...")
vehicle.simple_goto(target)

time.sleep(20)
print("Mission complete.")
vehicle.close()

⚠️ Issue Encountered

During testing, the system connected successfully but got stuck in the following loop:

Araç başlatılıyor, GPS bekleniyor...
GUIDED moduna geçiliyor...
(repeating indefinitely)

🔍 Cause

The simulated drone could not obtain a valid GPS 3D fix, preventing arming and guided mode activation.

🧰 Attempts & Troubleshooting

Launched SITL with GPS parameter:

sim_vehicle.py -v ArduCopter -L KSFO --gps --console --map


Disabled arming check for debugging:

param set ARMING_CHECK 0


Verified correct connection port (127.0.0.1:14550 or 127.0.0.1:5760).

🚧 Current Project Status
Stage	Status	Description
SITL setup	✅ Completed	Gazebo and ArduPilot successfully integrated
DroneKit connection	✅ Successful	Vehicle connected and initialized
GPS lock	⚠️ Failed	Stuck in “waiting for GPS” loop
Guided mode & movement	❌ Not achieved	Pending GPS fix to proceed
