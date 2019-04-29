#! /usr/bin/python3

from mido import MidiFile
import os
import math
import time

MODEL = "hierdec-mel_16bar"

RDir = "temp"
IDir = "Samples3"
os.makedirs(RDir, exist_ok=True)
os.makedirs(IDir, exist_ok=True)

BDir = "raw_buffer"
os.makedirs(BDir, exist_ok=True)
BThresh = 20

#NOTE : Req folder Music_VAE_models containing requistite MODEL

GenString = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=sample --num_outputs={1} --output_dir={2}"
IntString = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=interpolate --num_outputs={1} --input_midi_1={3} --input_midi_2={4} --output_dir={2}"

def generate(n, outDir) : os.system(GenString.format(MODEL, n, outDir))
def interpolate(n, outDir, f1, f2) : os.system(GenString.format(MODEL, n ,outDir, f1, f2))

def fill_buffer():
    while True:
        Blen = len(os.listdir(BDir))
        if Blen < BThresh:
            generate(BThresh-Blen, BDir)
        time.sleep(5)
fill_buffer()

def tempo_checker():
	tempo_check = 100
	location = "Raw_Buffer"
	cd = os.listdir(location)
	if '.DS_Store' in cd : cd.remove('.DS_Store') #MAC specific file removal
	for i in cd:
		fulloc = location+'/'+i
		print(fulloc)
		mid = MidiFile(fulloc)
		x = [i.time for i in mid.tracks[1]]
		tempo = sum(x)/len(x)

		if tempo >= tempo_check:
			outputDirectory = "High"
		else:
			outputDirectory = "Low"

		shutil.move(fulloc, outputDirectory)
		print("Song: {}\t Avg Tempo : {}\t OutputDirectory : {}".format(fulloc,round(tempo,2),outputDirectory))

#---------------------------------------------------------------------------------

'''
mid = MidiFile('Trio_Samples/samples/hierdec-trio_16bar_sample_2019-04-19_115005-001-of-002.mid')
for j in mid.tracks:
    print("\n{} :".format(j))
    x=[]
    y=[]
    for i in j:
        try:
            x.append(i.note%12)
            y.append(math.floor(i.note/12))
        except:
            continue
    print(x)
    print(y)
    #print(sum(x)/len(x), end='')
    #print(sum(x[:30])/30, end='')
    #print(sum(x[-30:])/30)

'''

#---------------------------------------------------------------------------------

def filter_tempo(location):
    threshold = 30
    cd = os.listdir(location)
    if '.DS_Store' in cd : cd.remove('.DS_Store') #MAC specific file removal
    for i in cd:
        fulloc = location+'/'+i
        mid = MidiFile(fulloc)
        x = [i.time for i in mid.tracks[1]]
        start = sum(x[:threshold])/threshold
        end = sum(x[-threshold:])/threshold
        print('{} : {} -> {}'.format(i,start,end))
        #try using print
        '''
        try:
            os.remove(filename)
        except OSError:
            pass
        '''

def rand_sample_10():
    string = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=sample --num_outputs=10 --output_dir={1}".format(MODEL,RDir)
    os.system(string)

def interpolate_2(file1,file2):
    string = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=interpolate --num_outputs=10 --input_midi_1={1} --input_midi_2={2} --output_dir={3}".format(MODEL, RDir+file1, RDir+file2, IDir)
    os.system(string)

def getFiles(location):
    return [i for i in ( os.listdir(location) if location else os.listdir() ) if i != '.DS_Store']

def interpolate_all(inputDir, outputDir):
    sList = sorted(getFiles('samples2'))
    for i in range(len(sList)-2):
        interpolate_2(sList[i],sList[i+1])


#filter_tempo('Trio_Samples/samples')
#filter_tempo('Trio_Samples/samples2')
#filter_tempo('samples2')

#rand_sample_10("Samples2")
#interpolate_2("/hierdec-trio_16bar_sample_2019-04-25_104923-000-of-010.mid","/hierdec-trio_16bar_sample_2019-04-25_104923-001-of-010.mid")

'''
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
'''