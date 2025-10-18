# DroneKit-Gazebo-Mission-Project
# =====================================================
# 🚁 DroneKit-Gazebo Mission Project
# =====================================================

# 👩‍💻 Author: Melda Yüce
# 🎓 Computer Engineering Student | AI • Embedded Systems • Web Development
# 📎 GitHub: https://github.com/MeldaYuceee
# 📬 Contact: meldayuce4@gmail.com

# -----------------------------------------------------
# 🧠 Project Summary
# -----------------------------------------------------
# This project simulates an autonomous drone mission in Gazebo using DroneKit-Python.
# The goal: connect to a simulated ArduCopter (SITL), switch to GUIDED mode,
# and make the drone fly from a defined start point to a target waypoint.

# -----------------------------------------------------
# ⚙️  Environment Setup
# -----------------------------------------------------

# 1️⃣ Create a project directory
mkdir dronekit_gazebo_project
cd dronekit_gazebo_project

# 2️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate        # (Windows PowerShell)
# or
source .venv/bin/activate            # (Linux/Mac)

# 3️⃣ Install required packages
pip install dronekit dronekit-sitl mavproxy

# 4️⃣ Verify installation
pip list | grep dronekit

# -----------------------------------------------------
# 🚀 Run the Simulation
# -----------------------------------------------------

# Launch ArduCopter SITL with Gazebo integration and GPS enabled
sim_vehicle.py -v ArduCopter -L KSFO --gps --console --map

# Open a second terminal and activate the environment again
source .venv/Scripts/activate

# Run the Python control script
python main.py

# -----------------------------------------------------
# 🧩 main.py Summary
# -----------------------------------------------------
# Connects to SITL drone, waits for GPS, switches to GUIDED mode,
# takes off to 10m altitude, then flies to target waypoint.

cat main.py
# from dronekit import connect, VehicleMode, LocationGlobalRelative
# import time
#
# print("Connecting to vehicle...")
# vehicle = connect('127.0.0.1:14550', wait_ready=True)
#
# print("Arming drone...")
# vehicle.mode = VehicleMode("GUIDED")
# vehicle.armed = True
# time.sleep(3)
#
# print("Taking off...")
# vehicle.simple_takeoff(10)
#
# target = LocationGlobalRelative(37.874, -122.302, 10)
# print("Going to target waypoint...")
# vehicle.simple_goto(target)
#
# time.sleep(20)
# print("Mission complete.")
# vehicle.close()

# -----------------------------------------------------
# ⚠️  Issue Encountered
# -----------------------------------------------------
# During tests, the system connected successfully but got stuck in:
#
#   Araç başlatılıyor, GPS bekleniyor...
#   GUIDED moduna geçiliyor...
#
# The script repeated these logs indefinitely.

# Diagnosis:
#   - SITL didn’t provide a valid GPS 3D fix.
#   - DroneKit couldn’t arm or switch to GUIDED mode.

# -----------------------------------------------------
# 🧰  Debug Commands (Solutions Tried)
# -----------------------------------------------------

# Option 1: Disable arming check (allows arming without GPS)
param set ARMING_CHECK 0

# Option 2: Manually set GPS fix in SITL console (for debugging)
gpssim 37.874 -122.302 10

# Option 3: Check the MAVProxy connection port
# If MAVProxy says “Connected to 127.0.0.1:5760”, update main.py:
# vehicle = connect('127.0.0.1:5760', wait_ready=True)

# -----------------------------------------------------
# 🧠 Lessons Learned
# -----------------------------------------------------
# - DroneKit requires a GPS 3D fix before arming.
# - Gazebo + SITL port matching is critical.
# - Debugging flight modes teaches real autopilot logic.

# -----------------------------------------------------
# 🚧 Project Status
# -----------------------------------------------------
# Phase: Prototype / In Progress
# ✅ Connection established
# ❌ GPS lock issue (stuck in GUIDED mode loop)
# 🎯 Next step: enable GPS fix and complete waypoint mission

# -----------------------------------------------------
# 🧭 Final Note
# -----------------------------------------------------
# "Every failed test is progress — debugging is part of the flight."
