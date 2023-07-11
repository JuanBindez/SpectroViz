# this is part of the SpectroViz project.
#
# Release: v0.1.dev
#
# Copyright ©  2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import os
import random
import datetime

import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv


def rec_audio():
    freq = 44100
    duration = int(input("Digite quantos segundos de gravação você quer >>"))
    recording = sd.rec(int(duration * freq),  
                    samplerate=freq, channels=2)

    name_file = str(datetime.datetime.now())

    sd.wait()
    #write("pyrec1_" + name_file, freq, recording) 
    wv.write("rec-" + name_file, recording, freq, sampwidth=2)

    os.system("clear")
    print("GRAVAÇÃO CONCLUÍDA!")
    print("Salvo com o nome: pyrec1_" + name_file + ".wav")
