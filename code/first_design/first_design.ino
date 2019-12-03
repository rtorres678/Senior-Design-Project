const int photoResistor1 = A0;
const int photoResistor2 = A1;
const int photoResistor3 = A2;
const int piezoSpeaker = 3;
const int greenPin = 6;
const int bluePin = 7;              // red led
int sensor1, sensor2, sensor3;
int counter;

void setup()
{
  Serial.begin(9600);
  counter = 1;
  pinMode(piezoSpeaker, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop()
{
  sensor1 = analogRead(photoResistor1);
  Serial.println(sensor1);
  //sensor2 = analogRead(photoResistor2);
  //sensor3 = analogRead(photoResistor3);

  if(counter){
    if(sensor1 >= 1000){
      counter = 0;
    }
  }else{
  if(sensor1 < 1000){ 
    tone(piezoSpeaker, 440, 100);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);
  }
  else {
    digitalWrite(piezoSpeaker, 0);
    digitalWrite(bluePin, HIGH);
    digitalWrite(greenPin, LOW);
  }
  }
    /*
  if(sensor2 > 500) 
    tone(piezoSpeaker, 494, 100);
  else
    digitalWrite(piezoSpeaker, 0);
  if(sensor3 > 500) 
    tone(piezoSpeaker, 523, 100);
  else
    digitalWrite(piezoSpeaker, 0);
    */
}
