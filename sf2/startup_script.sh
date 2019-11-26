#! /bin/sh
#fluidsynth -i -s -a alsa /home/pi/Desktop/sf2/JR_sax.sf2 /home/pi/Desktop/sf2/Test_-_test1.mid
lxterminal -e fluidsynth -s -a alsa /home/pi/Desktop/sf2/JR_sax.sf2 -g 6 & 
sleep 2; aconnect 20: 128:
lxterminal -e python /home/pi/fluidSynthGUI/gui.py &
if [ $? -eq 0 ]
then
    echo "Connection established."
    exit 0
else
    echo "Failed to connect. Terminating Fluidsynth..."
    pkill fluidsynth
    clear
    exit 1
fi

    
