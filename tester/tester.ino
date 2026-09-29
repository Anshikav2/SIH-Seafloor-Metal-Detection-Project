void setup() {
  Serial.begin(115200); // Matches the Python serial configuration
}

void loop() {
  // Generate a steady baseline value between 100 and 150
  int testValue = random(100, 150);
  
  // Randomly inject a spike every so often to test dashboard reactivity
  if (random(0, 40) == 1) {
    testValue = random(400, 650);
  }

  Serial.println(testValue);
  delay(50); // Send updates ~20 times per second
}
