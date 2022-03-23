int FSR_Pin = A0; //analog pin 0
int buzzer = A1;
int led = A2;

int time = 1;

void setup() {
  Serial.begin(9600);
  pinMode(A1,OUTPUT);
  pinMode(A2,OUTPUT);
}

void loop() {
  delay(1000);
  int FSRReading = analogRead(FSR_Pin);

  if(FSRReading > 0)
  {
    if(time >= 8)digitalWrite(A1,HIGH);
      
    digitalWrite(A2,HIGH);
    Serial.print(time);
    Serial.println(" 초 동안 눌림");
    time++;
  }


  
  else 
  {
    digitalWrite(A1,LOW);
    digitalWrite(A2,LOW);
    time = 1;
  }
  
  Serial.println(FSRReading);


}
