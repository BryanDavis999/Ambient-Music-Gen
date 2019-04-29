#! /usr/bin/python3

from mido import MidiFile
import os
import math

mid = MidiFile('Piano_Samples/samples/hierdec-mel_16bar_sample_2019-04-17_234251-000-of-002.mid')
everyNote = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

f = open("notes.txt","w")
for j in mid.tracks:
    notes = []
    for i in j:
        try:
            notes.append(i.note)
        except:
            print("No note attribute")

    notes_in_readable_form = []
    for i in  notes:
        notes_in_readable_form = "{}{} ".format(everyNote[i%12],str(math.floor(i/12)))
        f.write(notes_in_readable_form)
f.close()