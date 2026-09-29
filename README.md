# 🌊 SIH Seafloor Magnetic Anomaly Detection System

> **Smart India Hackathon (SIH) Project** – A low-cost seafloor metal detection and real-time sensor monitoring system.

This repository contains the software pipeline and user interface for an Arduino-based Pulse Induction (PI) marine metal detector. The system bridges raw hardware signals into a noise-gated Python environment and visualizes the magnetic anomalies in real-time through a Streamlit dashboard.

## ✨ Core Features

* **Real-Time Data Pipeline:** Reads transient magnetic decay from an Arduino serial connection, applying firmware-level Exponential Moving Average (EMA) filtering alongside a Python software noise gate.
* **Dynamic Calibration:** Features a 5-second environmental sampling mode that zeroes the baseline according to local magnetic interference (e.g., mineral-heavy sand vs. plain water).
* **Hysteresis Anomaly Detection:** Utilizes adaptive dual-threshold logic (Trigger and Reset thresholds) to prevent signal bounce from counting a single target as multiple false-positive anomalies.
* **Live Dashboard Visualization:** High-contrast Streamlit UI designed for pitch presentations, featuring real-time line charts, dynamic alert boxes, and CSV data logging for post-analysis.

## 📂 Repository Structure

* `app.py` — The main Streamlit dashboard application handling the UI, calibration logic, and real-time graphing.
* `serial_reader.py` — The primary Python bridge script that reads raw serial data from the Arduino, applies the threshold noise gate, and routes output to CSV buffers.
* `ide_to_python.py` — Additional testing script for Arduino serial data processing validation.
* `tester/` — Directory containing the Arduino sketch utilized for testing serial output generation.
* `data/` — Directory used by the dashboard to save detailed session logs (`session_log.csv`) containing timestamps and anomaly events.
* `live_bridge.csv` — Temporary pipeline file storing raw, unfiltered data straight from the microcontroller.
* `processed_data.csv` — Pipeline file storing clean, zero-gated mathematical data read by the dashboard.

## 🛠️ Hardware Requirements

To replicate the physical prototype, you will need:
* Arduino Uno/Nano (or compatible microcontroller)
* Pulse Induction Search Coil (Custom wound)
* LM324 Operational Amplifier (Front-end signal conditioning)
* IRF520 MOSFET (Pulse driving)
* Clamping diodes and damping resistors

## 🚀 Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anshikav2/SIH-Seafloor-Metal-Detection-Project.git
   cd SIH-Seafloor-Metal-Detection-Project
   ```

2. **Install dependencies:**
   Ensure you have Python 3.8+ installed. Install the required packages:
   ```bash
   pip install streamlit pandas numpy pyserial
   ```

3. **Flash the Hardware:**
   Upload the primary PI detection sketch to your Arduino via the Arduino IDE. Ensure the baud rate matches the configuration in `serial_reader.py`.

## 💻 Running the System

To launch the full end-to-end detection system, you need to run two terminal instances simultaneously.

**Terminal 1: Start the Data Bridge**
Connect the Arduino via USB and launch the serial reader to begin logging and filtering data:
```bash
python serial_reader.py
```

**Terminal 2: Launch the Dashboard**
Initialize the Streamlit UI to monitor the live feed:
```bash
streamlit run app.py
```

## 👥 Contributors
Developed for the Smart India Hackathon by **ShobhitLayal** and **Anshika**.
