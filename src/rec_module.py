import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv
import os
import random
import datetime

freq = 44100
duration = int(input("Digite quantos segundos de gravação você quer >>" + Color.RESET))
recording = sd.rec(int(duration * freq),  
                   samplerate=freq, channels=2)

name_file = str(datetime.datetime.now())

sd.wait()
#write("pyrec1_" + name_file, freq, recording) 
wv.write("rec-" + name_file, recording, freq, sampwidth=2)

os.system("clear")
print("GRAVAÇÃO CONCLUÍDA!")
print("Salvo com o nome: pyrec1_" + name_file + ".wav")
