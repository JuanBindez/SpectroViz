import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Configurações do espectrograma
sample_rate = 4100  # Taxa de amostragem (amostras por segundo)
duration = 40  # Duração da gravação em segundos
window_size = 1024  # Tamanho da janela para cálculo do espectrograma
overlap = int(window_size / 2)  # Sobreposição entre as janelas

# Inicializa os dados do espectrograma
frequencies = np.arange(window_size // 2 + 1) * sample_rate / window_size
times = np.arange(0, duration, duration / window_size)
spectrogram_data = np.zeros((window_size // 2 + 1, len(times)))

# Configuração inicial do espectrograma
im = plt.imshow(10 * np.log10(spectrogram_data), aspect='auto', origin='lower', cmap='inferno')

# Função para atualizar o espectrograma em tempo real
def update_spectrogram(indata, frames, time, status):
    global spectrogram_data

    # Calcula o espectrograma
    frequencies, times, new_spectrogram_data = plt.specgram(indata[:, 0], NFFT=window_size, Fs=sample_rate, noverlap=overlap)

    # Atualiza os dados do espectrograma
    spectrogram_data = np.roll(spectrogram_data, -1, axis=1)
    spectrogram_data[:, -1] = np.abs(new_spectrogram_data[:, 0])

    # Atualiza os dados da imagem do espectrograma
    im.set_array(10 * np.log10(spectrogram_data))

    # Retorna uma lista de artistas para atualização
    return [im]

# Configuração da gravação de áudio
stream = sd.InputStream(callback=update_spectrogram, channels=1, samplerate=sample_rate)
stream.start()
sd.sleep(int(duration * 1000))
stream.stop()
stream.close()

# Exibe o espectrograma final
plt.colorbar(label='Intensidade (dB)')
plt.ylabel('Frequência (Hz)')
plt.xlabel('Tempo (s)')
plt.title('Espectrograma em Tempo Real')
plt.show()
