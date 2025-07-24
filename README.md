# 🛩️ Basic Drone Flight Simulator (Python)

A beginner-friendly console-based drone simulator in Python. Simulates simple drone behavior such as takeoff, movement, rotation, and landing.

---

## 🚀 Features

- `takeoff()`: Start flight
- `land()`: Land the drone
- `move_forward()`: Move forward in Y-axis
- `move_up()` / `move_down()`: Ascend/descend in Z-axis
- `rotate_left()` / `rotate_right()`: Change orientation (yaw)
- `status()`: Print current drone status

---

## 🧠 How It Works

This simulator uses a simple Python class to manage drone state (position, yaw, flying status). It runs via command line and logs each command's effect.

---

## 📦 Requirements

No external libraries required. Just run with Python 3:

```bash
python drone_simulator.py
