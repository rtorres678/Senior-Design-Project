// setting up pin
int photo_resistor [12] = {14,15,16,17,18,19,20,21,22,23,39,38};
int midi_notes[12] = {48,49,50,51,52,53,54,55,56,57,58,59};
int note_playing [12] = {0,0,0,0,0,0,0,0,0,0,0,0};
int laser_1 = 1;

// threshold value for the photoresistor input
int light_threshold = 500;

//MIDI channel
const int channel = 1;

// the setup routine runs once when you press reset:
void setup() {
  // initialize the pin as input/output
  for (int i = 0; i < 12; i++){
    pinMode(photo_resistor[i], INPUT);
  }
  pinMode(laser_1, OUTPUT);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  for (int i = 0; i < 12; i++){
    if(analogRead(photo_resistor[i]) < light_threshold && !note_playing[i]){
      usbMIDI.sendNoteOn(midi_notes[i], 99, channel);
      Serial.println(i);
      note_playing[i] = 1;
    } else if (analogRead(photo_resistor[i]) > light_threshold && note_playing[i]){
      usbMIDI.sendNoteOff(midi_notes[i], 99, channel);
      note_playing[i] = 0;
    }
  }
}
