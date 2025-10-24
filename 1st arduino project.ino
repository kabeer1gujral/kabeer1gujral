int pirPin = 15;
void setup() {
 Serial.begin(115200);
 pinMode(pirPin, INPUT);
}
void loop() {
 int pirValue = digitalRead(pirPin);
 if (pirValue == HIGH) {
 Serial.println("Motion detected!");
 } 
}
