import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import soundfile as sf
import os


INPUT_FILE = "input.wav"         
OUTPUT_FILE = "output_clean.wav"     
OUTPUT_DIR = "spectrogram_examples"  

os.makedirs(OUTPUT_DIR, exist_ok=True)


if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"{INPUT_FILE} not found in {os.getcwd()}")

rate, data = wav.read(INPUT_FILE)

if len(data.shape) == 2:
    data = data.mean(axis=1)

print(f"Sample rate: {rate} Hz")
print(f"Audio duration: {len(data)/rate:.2f} seconds")


time = np.linspace(0, len(data)/rate, num=len(data))
plt.figure(figsize=(12, 4))
plt.plot(time, data)
plt.title("Time Domain (Waveform)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.savefig(os.path.join(OUTPUT_DIR, "waveform.png"))
plt.close()

fft_data = np.fft.fft(data)
freqs = np.fft.fftfreq(len(data), 1/rate)

plt.figure(figsize=(12, 4))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_data)[:len(freqs)//2])
plt.title("Frequency Domain (FFT Spectrum)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.savefig(os.path.join(OUTPUT_DIR, "fft_spectrum.png"))
plt.close()


cutoff = 3000  
fft_data[np.abs(freqs) > cutoff] = 0


cleaned_data = np.fft.ifft(fft_data).real
cleaned_data = cleaned_data / np.max(np.abs(cleaned_data))  

sf.write(OUTPUT_FILE, cleaned_data, rate)
print(f" Cleaned audio saved as {OUTPUT_FILE}")


plt.figure(figsize=(12, 4))
plt.specgram(data, Fs=rate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title("Spectrogram - Original")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar(label="Intensity (dB)")
plt.savefig(os.path.join(OUTPUT_DIR, "spectrogram_before.png"))
plt.close()

plt.figure(figsize=(12, 4))
plt.specgram(cleaned_data, Fs=rate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title("Spectrogram - Cleaned")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar(label="Intensity (dB)")
plt.savefig(os.path.join(OUTPUT_DIR, "spectrogram_after.png"))
plt.close()

print(f"Spectrogram images saved in '{OUTPUT_DIR}' folder.")
