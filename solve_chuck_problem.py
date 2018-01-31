import scipy.io.wavfile as wav
import soundfile
import os

for filename in os.listdir("."):
    if filename.endswith(".wav"):
    	data, samplerate = soundfile.read(filename)
    	soundfile.write(filename, data, samplerate, subtype='PCM_16')
    	fs, signal = wav.read(filename)
    	print(fs)
    	print(signal)