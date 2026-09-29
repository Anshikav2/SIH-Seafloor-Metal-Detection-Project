import serial
import csv
import os
from datetime import datetime

# Initialize both files
with open("live_bridge.csv", "w", newline="") as f1, open("processed_data.csv", "w", newline="") as f2:
    csv.writer(f1).writerow(["Timestamp", "Raw_Signal"])
    csv.writer(f2).writerow(["Timestamp", "Signal"]) # Streamlit looks for "Signal"

def read_sensor(port, baudrate=115200):
    try:
        ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        print(f"\nConnected to {port}")
        print("Logging raw to live_bridge.csv and processed to processed_data.csv...\n")

        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            
            if line:
                try:
                    raw_signal = float(line)
                    now = datetime.now().strftime("%H:%M:%S")
                    
                    # 1. Save the untouched raw data
                    with open("live_bridge.csv", "a", newline="") as f1:
                        csv.writer(f1).writerow([now, raw_signal])
                        
                    # ==========================================
                    # 2. YOUR PYTHON PROCESSING LOGIC
                    # ==========================================
                    # Example: Subtract your resting baseline of ~150 so the graph rests at 0
                    processed_signal = raw_signal # -40
                    
                    # Example: Cap negative values to 0 to keep the UI clean
                    if processed_signal -15 < 0:
                        processed_signal = 0

                        
                    # 3. Save the processed data for Streamlit
                    with open("processed_data.csv", "a", newline="") as f2:
                        csv.writer(f2).writerow([now, processed_signal])
                        
                    print(f"Raw: {raw_signal:.1f} | Processed: {processed_signal:.1f}")

                except ValueError:
                    pass 
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_sensor("COM6") # Update port if necessary