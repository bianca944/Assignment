const int tempPin = A0;   
const int buzzerPin = 9;   

float threshold = 30.0;    
void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  int sensorValue = analogRead(tempPin);

  // Conversie la grade Celsius
  float voltage = sensorValue * (5.0 / 1023.0);
  float temperatureC = (voltage - 0.5) * 100.0;

  Serial.print("Temperatura: ");
  Serial.print(temperatureC);
  Serial.print(" °C | Timp: ");
  Serial.println(millis() / 1000);

  if (temperatureC > threshold) {
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(buzzerPin, LOW);
  }

  delay(2000);
}
