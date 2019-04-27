#! /usr/bin/python3

from mido import MidiFile
import os
import serial
import serial.tools.list_ports
import time

high_tempo = 200
low_tempo  = 100

def get_avg_tempo(location):
    cd = os.listdir(location)
    if '.DS_Store' in cd : cd.remove('.DS_Store') #MAC specific file removal
    for i in cd:
        fulloc = location+'/'+i
        mid = MidiFile(fulloc)
        x = [i.time for i in mid.tracks[1]]
        tempo = sum(x)/len(x)

        if tempo >= high_tempo:
            outputDir = "High"
        elif tempo <= low_tempo:
            outputDir = "Low"
        else:
            outputDir = "Mid"

        print("Song: {}\t Avg Tempo : {}\t OutputDir : {}".format(fulloc,round(tempo,2),outputDir))

get_avg_tempo('Piano_Samples/Samples2')
