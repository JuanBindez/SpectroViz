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


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def spectrogram_extract():
    file_path = filedialog.askopenfilename()
    sample_rate, audio_data = wavfile.read(file_path)

    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)

    frequencies, times, spectrogram_data = spectrogram(audio_data, sample_rate)

    plt.figure(figsize=(15, 6))

    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto', cmap='plasma')  # Mudando a cor para 'hot'
    plt.colorbar(label='Intensity (dB)')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title('SpectroViz v0.1.dev')

    #plt.xlim(0, 2000)

    plt.show()

