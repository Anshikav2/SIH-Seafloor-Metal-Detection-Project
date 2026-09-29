import time
import serial

# Configure your port and baud rate (matching Arduino)
PORT = "COM6"  # Change to your actual port if needed
BAUD = 115200

try:
  ser = serial.Serial(PORT, BAUD, timeout=1)
  time.sleep(2)  # Allow connection to settle
  print(f"Connected to Arduino on {PORT} at {BAUD} baud.")
except Exception as e:
  print(f"Failed to connect to serial port: {e}")
  exit()


def process_data(raw_value):
  """Light processing function for your metal detector stream."""
  # Example: filter noise or scale the value if needed
  processed_value = int(raw_value)
  return processed_value

def update_dashboard(value):
  """Hook this function into your existing dashboard backend."""
  # TODO: Pass 'value' to your dashboard's data source, WebSocket, or CSV file
  pass


if __name__ == "__main__":
  print("Listening for live serial data... Press Ctrl+C to stop.")
  try:
    while True:
      if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8", errors="ignore").strip()

        # Ensure the line is a valid number before processing
        if line.isdigit():
          raw_val = int(line)
          clean_val = process_data(raw_val)

          # Send to your dashboard
          update_dashboard(clean_val)

          # Optional: print to verify real-time flow
          print(f"Live Data -> Raw: {raw_val} | Processed: {clean_val}")

  except KeyboardInterrupt:
    ser.close()
    print("\nSerial connection closed safely.")
