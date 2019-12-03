// setting up pin
int photo_resistor_1 = 14;
int photo_resistor_2 = 15;
int photo_resistor_3 = 16;
int photo_resistor_4 = 17;
int photo_resistor_5 = 18;
int photo_resistor_6 = 19;
int laser_1 = 1;
int piezo = 30;
int led_1 = 24;
int led_2 = 25;
int led_3 = 26;
int led_4 = 27;
int led_5 = 28;
int led_6 = 29;
// threshold value for the photoresistor input
int light_threshold = 900;

//MIDI channel
const int channel = 1;

int note1_playing = 0;
int note2_playing = 0;
int note3_playing = 0;
int note4_playing = 0;
int note5_playing = 0;
int note6_playing = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize the pin as input/output
  pinMode(photo_resistor_1, INPUT);
  pinMode(photo_resistor_2, INPUT);
  pinMode(photo_resistor_3, INPUT);
  pinMode(photo_resistor_4, INPUT);
  pinMode(photo_resistor_5, INPUT);
  pinMode(photo_resistor_6, INPUT);
  pinMode(laser_1, OUTPUT);
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
  pinMode(led_4, OUTPUT);
  pinMode(led_5, OUTPUT);
  pinMode(led_6, OUTPUT);

  digitalWrite(led_1, LOW);
  digitalWrite(led_2, LOW);
  digitalWrite(led_3, LOW);
  digitalWrite(led_4, LOW);
  digitalWrite(led_5, LOW);
  digitalWrite(led_6, LOW);
  
  //serial read start
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  //Serial.println(analogRead(photo_resistor_1));

  //if any of the photoresistor reads a value less than a threshold, play corresponding tone
  if (analogRead(photo_resistor_1) < light_threshold && !note1_playing) {
    //analogWrite(piezo, 10);
    usbMIDI.sendNoteOn(60, 99, channel);
    digitalWrite(led_1, HIGH);
    Serial.println(1);
    note1_playing = 1;
  } else if (analogRead(photo_resistor_1) > light_threshold && note1_playing){
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(60, 99, channel);
    digitalWrite(led_1, LOW);
    note1_playing = 0;
  }

  //Serial.println(analogRead(photo_resistor_2));
  if (analogRead(photo_resistor_2) < light_threshold && !note2_playing) {
    //analogWrite(piezo, 180);
    usbMIDI.sendNoteOn(62, 99, channel);
    digitalWrite(led_2, HIGH);
    Serial.println(2);
    note2_playing = 1;
  } else if (analogRead(photo_resistor_2) > light_threshold && note2_playing){
    digitalWrite(led_2, LOW);
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(62, 99, channel);
    note2_playing = 0;
  }

  if (analogRead(photo_resistor_3) < light_threshold && !note3_playing) {
    //analogWrite(piezo, 350);
    usbMIDI.sendNoteOn(64, 99, channel);
    digitalWrite(led_3, HIGH);
    Serial.println(3);
    note3_playing = 1;
  } else if (analogRead(photo_resistor_3) > light_threshold && note3_playing){
    digitalWrite(led_3, LOW);
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(64, 99, channel);
    note3_playing = 0;
  }

  if (analogRead(photo_resistor_4) < light_threshold && !note4_playing) {
    //analogWrite(piezo, 520);
    usbMIDI.sendNoteOn(65, 99, channel);
    digitalWrite(led_4, HIGH);
    Serial.println(4);
    note4_playing = 1;
  } else if (analogRead(photo_resistor_4) > light_threshold && note4_playing){
    digitalWrite(led_4, LOW);
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(65, 99, channel);
    note4_playing = 0;
  }

  if (analogRead(photo_resistor_5) < light_threshold && !note5_playing) {
    //analogWrite(piezo, 690);
    usbMIDI.sendNoteOn(67, 99, channel);
    digitalWrite(led_5, HIGH);
    Serial.println(5);
    note5_playing = 1;
  } else if (analogRead(photo_resistor_5) > light_threshold && note5_playing){
    digitalWrite(led_5, LOW);
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(67, 99, channel);
    note5_playing = 0;
  }

  if (analogRead(photo_resistor_6) < light_threshold && !note6_playing) {
    //analogWrite(piezo, 860);
    usbMIDI.sendNoteOn(69, 99, channel);
    digitalWrite(led_6, HIGH);
    Serial.println(6);
    note6_playing = 1;
  } else if (analogRead(photo_resistor_6) > light_threshold && note6_playing){
    digitalWrite(led_6, LOW);
    //analogWrite(piezo, 0);
    usbMIDI.sendNoteOff(69, 99, channel);
    note6_playing = 0;
  }
  //Serial.println();
}
