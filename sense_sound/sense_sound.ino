int soundDetectedPin = 10; // Use Pin 10 as our Input
int soundDetectedVal = HIGH; // This is where we record our Sound Measurement

void setup () {
  Serial.begin(9600);
  pinMode (soundDetectedPin, INPUT) ; // input from the Sound Detection Module
}

void loop () {
  soundDetectedVal = digitalRead (soundDetectedPin) ; // read the sound alarm time
  Serial.println(soundDetectedVal);
  // Serial.write(soundDetectedVal);
  delay(500);
}
