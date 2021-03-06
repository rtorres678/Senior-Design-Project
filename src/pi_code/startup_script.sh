#! /bin/sh
#fluidsynth -i -s -a alsa /home/pi/Desktop/sf2/JR_sax.sf2 /home/pi/Desktop/sf2/Test_-_test1.mid
echo "Starting Fluidsynth..."
cd /home/pi/Senior-Design-Project/src/pi_code/
lxterminal -e fluidsynth -s -a alsa /home/pi/Senior-Design-Project/src/pi_code/sf2/JR_sax.sf2 -g 6 & 
echo "Done\nSearching for MIDI device..."
sleep 5; aconnect 20: 128:
if [ $? -eq 0 ]
then
    echo "Connection established.\nStarting gui..."
    lxterminal -e python3 /home/pi/Senior-Design-Project/src/pi_code/gui.py &
    exit 0
else
    echo "Failed to connect. Terminating Fluidsynth..."
    pkill fluidsynth
    clear
    exit 1
fi

    
