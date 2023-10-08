#include "Arduino_SensorKit.h"
#define light 6 
const int trigPin = 3;
const int echoPin = 2;
long duration;
int distanceCm;

void setup() {
  Oled.begin();
  Oled.setFlipMode(true); // Sets the rotation of the screen display
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(light, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.034 / 2;

  if (distanceCm <20)
  {
    Oled.setFont(u8x8_font_chroma48medium8_r); 
    Oled.setFont(u8x8_font_chroma48medium8_r); 

    digitalWrite(light, HIGH); 
    Oled.refreshDisplay(); Oled.setCursor(0, 50);
    Oled.print("PERSON DETECTED");
    Oled.setCursor(0, 30);
    Oled.print("Turn on Light");
    Oled.refreshDisplay();  
    delay(10);
  }else 
  {
    digitalWrite(light, LOW); 
    Oled.setFont(u8x8_font_chroma48medium8_r); 

    Oled.setCursor(0, 50);
    Oled.print("Turn off Light ");
    Oled.setCursor(0, 30);
    Oled.print("NO-ONE HERE. ");
    Oled.refreshDisplay(); 
    delay(10);
  }

  Serial.print("Distance: ");
  Serial.print(distanceCm);
  Serial.print(", Status: ");
  Serial.println((distanceCm < 20) ? "Person Detected" : "No One Here");

}
