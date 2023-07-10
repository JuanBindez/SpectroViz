import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# Load the audio file
sample_rate, audio_data = wavfile.read('Nirvana-Drain-You-_Audio_.wav')

# Convert stereo audio to mono if needed
if len(audio_data.shape) > 1:
    audio_data = audio_data.mean(axis=1)

# Compute the spectrogram
frequencies, times, spectrogram_data = spectrogram(audio_data, sample_rate)

# Plot the spectrogram
plt.figure(figsize=(10, 6))
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
plt.colorbar(label='Intensity (dB)')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.title('Spectrogram')
plt.show()
