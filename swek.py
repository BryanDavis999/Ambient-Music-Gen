#! /usr/bin/python3

from mido import MidiFile
import os
import math
import time
from threading import Thread

import serial
import serial.tools.list_ports

MODEL = "hierdec-mel_16bar"

BDir = "raw_buffer"
os.makedirs(BDir, exist_ok=True)
RBThresh = 40 #numeric threshold of files in the raw buffer

FDir = "final_buffer"
os.makedirs(FDir+"/high", exist_ok=True)
os.makedirs(FDir+"/low", exist_ok=True)
FBThresh = 20 #numeric threshold of files in the final buffer

TThresh = 100 #threshold to tell whether music is high or low tempo
NThresh = 4 #threshold to measure ambient noise in surroundings

playlist = "playlist"
os.makedirs(playlist, exist_ok=True)
if(os.listfir(playlist)):
    PNext = int(sorted(os.listdir(playlist))[-1].split('.')[0])
else:
    PNext = 1

#NOTE : Req folder Music_VAE_models containing requistite MODEL

#--------------------------------------------------------------- INIT
GenString = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=sample --num_outputs={1} --output_dir={2}"
IntString = "music_vae_generate --config={0} --checkpoint_file=Music_VAE_models/{0}.tar --mode=interpolate --num_outputs={1} --input_midi_1={3} --input_midi_2={4} --output_dir={2}"

def generate(n, outDir) : os.system(GenString.format(MODEL, n, outDir))
def interpolate(n, outDir, f1, f2) : os.system(GenString.format(MODEL, n ,outDir, f1, f2))
#---------------------------------------------------------------
    
#--------------------------------------------------------------- THREAD 1
def fill_buffers():
    while True:
        Blen = len(os.listdir(BDir))
        if Blen < RBThresh:
            generate(RBThresh-Blen, BDir)
        
        Hlen = len(os.listdir(FDir+"/high"))
        Llen = len(os.listdir(FDir+"/low"))
        mainLen = Hlen if Hlen<Llen else Llen
        
        if mainLen<FBThresh:
            cd = os.listdir(BDir)
            if '.DS_Store' in cd : cd.remove('.DS_Store') #MAC specific file removal
            for i in cd[:FBThresh-mainLen]:
                file_loc = BDir+'/'+i
                mid = MidiFile(file_loc)
                x = [i.time for i in mid.tracks[1]]

                th = math.floor(len(x)*0.3)
                start = sum(x[:th])/th
                end = sum(x[-th:])/th
                avg = sum(x)/len(x)

                if(start>1.4*end or end>1.4*start):
                    os.remove(file_loc)
                else:
                    if avg > TThresh: os.rename(file_loc, FDir+"/high/"+i)
                    else: os.rename(file_loc, FDir+"/low/"+i)

                print('{} : {} -> {}'.format(i,start,end), end='\t')
                print("deleted" if start>1.4*end or end>1.4*start else "saved")
        
        time.sleep(5)

t1 = Thread(target = fill_buffers)
#t1.start()
#---------------------------------------------------------------

#--------------------------------------------------------------- THREAD 2
def get_arduino_port():
    ports_list = list(serial.tools.list_ports.comports())
    if ports_list:
        for p in ports_list:
            print(p)
            device = str(p.description)
            if device=="Generic CDC": #MAC Specific
                return p.device
            elif "ACM" in device: #Linux Specific
                return ("/dev/" + device)
            else:
                print("Arduino not found.\n")
    else:
        print("No device found.\n")

def mood_filter():
    print("\n")
    port = get_arduino_port()
    print("Arduino found in " + port)

    ser = serial.Serial(port, 9600)
    while True:
        s=0
        end_time = time.time()+10
        while time.time()<end_time:
            s+=int(ser.readline().decode())
        target = "high" if S>NThresh else "low"
        file_loc = FDir +'/'+ target
        file_loc += os.listdir(file_loc)[1]
        dest_loc = playlist+"/"+str(PNext)+".mid"
        PNext+=1
        if len(os.listdir(playlist))==0:
            os.rename(file_loc, dest_loc)
            os.system("mscore - o " +str(PNext)+".pdf " + dest_loc)
            os.system("lpr " +str(PNext)+".pdf)
        
        
t2 = Thread(target = final_filter)
#t2.start()
#--------------------------------------------------------------- 


                      
                      
                      
                      
                      
                      
                      
                      
                      
#FOR FUTURE DEVELOPMENT                      
'''
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

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
'''