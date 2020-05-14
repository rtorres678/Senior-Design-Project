#! /bin/sh
#fluidsynth -i -s -a alsa /home/pi/sf2_new/Harp.sf2 /home/pi/Desktop/sf2/Test_-_test1.mid

echo "Starting Fluidsynth..."

#lxterminal -e fluidsynth -s -a alsa /home/pi/sf2_new/strings.sf2 -g 2 & 
lxterminal -e fluidsynth -s -a alsa /home/pi/fluidsynth-kivy-test/sf2_new/Harp.sf2 -g 2 & 
#lxterminal -e fluidsynth -s -a alsa -o midi.autoconnect=1 /home/pi/sf2_new/strings.sf2 -g 2 & 

echo "Done\nSearching for MIDI device..."
sleep 2; aconnect 20: 128:
if [ $? -eq 0 ]
then
    echo "Connection established.\nStarting gui..."
    lxterminal -e python3 main.py &
    #exit 0
else
    echo "Failed to connect. Terminating Fluidsynth..."
    pkill fluidsynth
    #clear
    exit 1
fi

    
