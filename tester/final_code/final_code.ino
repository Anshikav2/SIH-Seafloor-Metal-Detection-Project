const int TX_PIN = 9;
int baseline = 0;
int buzzer =5;
float smoothedSignal = 0; // Added for smoothing

void setup() {
  Serial.begin(115200);
  pinMode(TX_PIN, OUTPUT);
  digitalWrite(TX_PIN, LOW);

  pinMode(buzzer, OUTPUT);
  digitalWrite(buzzer, LOW);
  
  // SAFE CALIBRATION: Fire actual short pulses to get the baseline
  long baselineSum = 0;
  for (int i = 0; i < 20; i++) {
    digitalWrite(TX_PIN, HIGH);
    delayMicroseconds(120);
    digitalWrite(TX_PIN, LOW);
    
    delayMicroseconds(20);
    baselineSum += analogRead(A0);
    delay(20); 
  }
  
  baseline = baselineSum / 20;
  smoothedSignal = baseline; // Start the filter at the baseline
}

void loop() {
  // YOUR EXACT WORKING TIMINGS
  digitalWrite(TX_PIN, HIGH);
  delayMicroseconds(120);
  digitalWrite(TX_PIN, LOW);

  // Wait for receiver transient
  delayMicroseconds(20);

  int rawSignal = analogRead(A0);

  // LIGHTWEIGHT FILTER: Smooths out the random jumps without lagging
  // It takes 60% of the old value and 40% of the new raw reading
  smoothedSignal = (smoothedSignal * 0.6) + (rawSignal * 0.4);

  // Print the clean signal to the terminal/dashboard
  Serial.println(smoothedSignal);
  if (smoothedSignal > 665){
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
  }
  delay(20);
}
