#! /bin/sh
#fluidsynth -i -s -a alsa /home/pi/Desktop/sf2/JR_sax.sf2 /home/pi/Desktop/sf2/Test_-_test1.mid
LOGFILE=/home/pi/Senior-Design-Project/src/pi_code/test.log
echo "$(date "+%m-%d-%Y %T") : Starting Fluidsynth..." >> $LOGFILE 2>&1 
cd /home/pi/Senior-Design-Project/src/pi_code/
lxterminal -e fluidsynth -s -a alsa /home/pi/Senior-Design-Project/src/pi_code/sf2/JR_sax.sf2 -g 6 & 
echo "Done\nSearching for MIDI device..." >> $LOGFILE 2>&1
sleep 5; aconnect 20: 128: >> $LOGFILE 2>&1
if [ $? -eq 0 ]
then
    echo "Connection established.\n$(date "+%m-%d-%Y %T") : Starting gui...\n\n" >> $LOGFILE 2>&1
    lxterminal -e python3 /home/pi/Senior-Design-Project/src/pi_code/gui.py &
    exit 0
else
    echo "$(date "+%m-%d-%Y %T") : ERROR Failed to connect. Terminating Fluidsynth...\n" >> $LOGFILE 2>&1
    pkill fluidsynth
    clear
    exit 1
fi

    
