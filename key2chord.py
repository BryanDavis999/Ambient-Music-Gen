#! /usr/bin/python3

from mido import MidiFile
import os
import math

mid = MidiFile('Trio_Samples/samples/hierdec-trio_16bar_sample_2019-04-19_115005-001-of-002.mid')
everyNote = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
print(type(everyNote))
for j in mid.tracks:
    notes = []
    for i in j:
        try:
            notes.append(i.note)
        except:
            print("No note attribute")
    print(notes)

    notes_in_readable_form = []
    for i in  notes:
        notes_in_readable_form.append(everyNote[i%12]+str(math.floor(i/12)))
    print(notes_in_readable_form)

def getFiles(location):
    return [i for i in ( os.listdir(location) if location else os.listdir() ) if i != '.DS_Store']




#filter_tempo('Trio_Samples/samples')
#filter_tempo('Trio_Samples/samples2')

#filter_tempo('Samples2')

#rand_sample_10("Samples2")