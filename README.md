# SPO₂ and Heart Rate Monitor using Smartphone Camera

This project presents a **non-invasive, low-cost method** to estimate **blood oxygen saturation (SPO₂)** and **heart rate** using a **smartphone camera** and **flashlight**.

It works based on the principle of **photoplethysmography (PPG)** — a technique that detects blood volume changes in the fingertip. The user places their finger over the smartphone camera and flashlight. The video stream is analyzed to detect color intensity changes (especially in the red and green channels), which reflect pulse and oxygen levels.

---

## 🔬 Project Objective

To design and implement a system that:
- Accurately captures **heart rate** from finger pulse signals
- Estimates **oxygen saturation (SPO₂)** using red-to-green light absorption ratios
- Uses only a **smartphone** and **Python**, without any external hardware
- Can be used as a basic health monitoring tool

---

## ✅ Features

- 📱 Uses any Android phone (via IP Webcam app)
- 🔴 Analyzes red and green color values from camera feed
- 🫀 Detects pulse using peak detection in signal
- 🩸 Calculates SPO₂ with a simplified ratio formula
- 🧠 Real-time processing and immediate result display
- 💻 Built using Python (OpenCV, NumPy, SciPy)

---

## 🧰 Technologies Used

| Component       | Technology                |
|----------------|----------------------------|
| Video Stream    | IP Webcam App (Android)   |
| Image Processing| OpenCV                    |
| Signal Analysis | NumPy, SciPy              |
| Visualization   | Matplotlib (optional)     |
| Language        | Python 3.x                |

## Output
