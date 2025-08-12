# SpectrumCraft: Fourier Analysis for Audio Signal Processing 

## Overview
This repository showcases my transition from "pure mathematics" in my B.Sc. (Mathematics) project to a "practical computer science application" during my MCA.

The original UG project explored "Fourier Analysis" — a mathematical method to decompose complex signals into simple sine and cosine waves.  
I extended this into a "Python-based Audio Signal Processing tool" using the "Fast Fourier Transform (FFT)" for real-world tasks such as noise reduction, speech spectrogram generation, and music frequency analysis.

---

## Features
- "UG Mathematics Project" — Original theoretical research on Fourier Analysis and applications.
- "CS Implementation" — Python FFT code for audio processing.
- "Audio Frequency Analysis" — View frequency spectrum of `.wav` files.
- "Noise Reduction" — Remove unwanted frequencies above a chosen cutoff.
- "Spectrogram Visualization" — Before & after comparison.

---

## How It Works
1. "Load Audio" → Read `.wav` file.
2. "FFT Analysis" → Convert waveform from time to frequency domain.
3. "Filter Noise" → Remove unwanted frequencies.
4. "Inverse FFT" → Rebuild clean audio signal.
5. "Save & Visualize" → Output `.wav` file and spectrogram images.

---

## Setup & Run Locally
### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/SpectrumCraft-Fourier-Analysis-for-Audio-Signal-Processing.git
cd SpectrumCraft-Fourier-Analysis-for-Audio-Signal-Processing

Install Dependencies 
pip install -r requirements.txt

Run this scripts 
python CS_Extension_Code/audio_fft_noise_reduction.py
