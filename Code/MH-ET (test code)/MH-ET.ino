// This code is not operational
#define FREQ_PIN 2 // Frequency input from HB100 connected to digital pin 5

unsigned long count;
unsigned long prevTime;
float speed;

void setup() {
  Serial.begin(9600);
  pinMode(FREQ_PIN, INPUT);
}

void loop() {
  count = pulseIn(FREQ_PIN, HIGH); // Measure the high time of the pulse in microseconds
  unsigned long currentTime = micros();

  // Calculate the frequency (in Hz)
  float frequency = 1000000.0 / count; // Frequency = 1 / Period

  // Calculate the speed (in m/s)
  // Speed = Frequency * Wavelength / 2
  // Assuming a wavelength of 0.0285 m for 10.525 GHz
  speed = frequency * 0.0285 / 2;

  // Print the speed
  Serial.print("Speed: ");
  Serial.print(speed);
  Serial.println(" m/s");

  // Wait for a second before the next reading
  delay(100);
}
