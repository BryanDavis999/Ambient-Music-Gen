#! /usr/bin/python3

from mido import MidiFile
import os
import math

low_midi = MidiFile('Low/hierdec-mel_16bar_interpolate_2019-04-17_234652-001-of-005.mid')
high_midi = MidiFile('High/hierdec-mel_16bar_interpolate_2019-04-17_234652-000-of-005.mid')

def getPitch(mid,pos) :
    # mid = MidiFile(file)
    j = mid.tracks[1]
    notes = []
    for i in range(0,len(j)):
        msg = j[i]
        if i != 0 and i != len(j)-1:
            notes.append(msg.note)
    # print(notes)
    pitch = math.floor(notes[pos]/12)
    return pitch

def high_to_low():
    high_pitch = getPitch(high_midi,-1)
    low_pitch = getPitch(low_midi,0)
    print("High to Low : high_pitch: {} \t low_pitch: {}".format(high_pitch,low_pitch))

def low_to_high():
    low_pitch = getPitch(low_midi,-1)
    high_pitch = getPitch(high_midi,0)
    print("Low to High : high_pitch: {} \t low_pitch: {}".format(high_pitch,low_pitch))

high_to_low()
low_to_high()