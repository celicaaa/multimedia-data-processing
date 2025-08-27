import librosa
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

audio_file = '01-a01.wav'
signal, sample_rate = librosa.load(audio_file, sr=22050)

print("Форма сигнала (количество отсчетов):", signal.shape)
print("Частота дискретизации:", sample_rate, "Гц")

#график аудио
plt.figure(figsize=(14, 5))
librosa.display.waveshow(signal, sr=sample_rate)
plt.title('Волновая форма аудиосигнала')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

# воспроизведение
sd.play(signal, samplerate=sample_rate)
sd.wait()

#спектр анализ
n_fft = 2048
ft = np.abs(librosa.stft(signal[:n_fft], hop_length=n_fft//2))
freqs = librosa.fft_frequencies(sr=sample_rate, n_fft=n_fft)

#линейный масштаб
plt.figure(figsize=(12, 6))
plt.plot(freqs, ft[:, 0])
plt.title('Спектр сигнала (линейная шкала)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.xlim(0, sample_rate//2)
plt.grid(True)
plt.show()

#логарифмический масштаб
plt.figure(figsize=(12, 6))
plt.semilogx(freqs, ft[:, 0])
plt.title('Спектр сигнала (логарифмическая шкала)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.xlim(20, sample_rate//2)
plt.grid(True, which="both", ls="-")
plt.show()

#спектрограмма каждого сигнала
X = librosa.stft(signal)
S_db = librosa.amplitude_to_db(np.abs(X), ref=np.max)
plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db, sr=sample_rate, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB', label='Уровень (дБ)')
plt.title('Спектрограмма сигнала')
plt.xlabel('Время (сек)')
plt.ylabel('Частота (Гц)')
plt.show()