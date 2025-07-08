import cv2
import numpy as np
import time
from collections import deque
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# --- Configuration ---
ROI = (100, 150, 100, 100)  # (y, x, h, w)
SAMPLE_TIME = 15  # seconds
FPS = 30
BUFFER_SIZE = SAMPLE_TIME * FPS

# Replace with your IP camera URL (from IP Webcam app)
cap = cv2.VideoCapture("http://192.0.0.4:8080/video")

# Buffers
red_buffer = deque(maxlen=BUFFER_SIZE)
green_buffer = deque(maxlen=BUFFER_SIZE)
timestamps = deque(maxlen=BUFFER_SIZE)

print("Collecting data for", SAMPLE_TIME, "seconds...")
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    y, x, h, w = ROI
    roi = frame[y:y+h, x:x+w]

    red = np.mean(roi[:, :, 2])
    green = np.mean(roi[:, :, 1])

    red_buffer.append(red)
    green_buffer.append(green)
    timestamps.append(time.time() - start_time)

    # Show ROI
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("IP Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if (time.time() - start_time) > SAMPLE_TIME:
        break

cap.release()
cv2.destroyAllWindows()

# ------------------------------
# SIGNAL PROCESSING
# ------------------------------

def process_signal(timestamps, red_buffer, green_buffer):
    times = np.array(timestamps)
    red = np.array(red_buffer)
    green = np.array(green_buffer)

    red = (red - np.mean(red)) / np.std(red)
    green = (green - np.mean(green)) / np.std(green)

    peaks, _ = find_peaks(green, distance=30)
    peak_intervals = np.diff(times[peaks])
    heart_rate = 60 / np.mean(peak_intervals)

    red_ac = np.max(red) - np.min(red)
    green_ac = np.max(green) - np.min(green)
    red_dc = np.mean(red)
    green_dc = np.mean(green)

    ratio = (red_ac / red_dc) / (green_ac / green_dc)
    spo2 = 100 - 5 * ratio  # Simplified formula

    return round(heart_rate), round(spo2)

hr, spo2 = process_signal(timestamps, red_buffer, green_buffer)
print(f"Heart Rate: {hr} bpm, SpO2: {spo2}%")
