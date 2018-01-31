import scipy.io.wavfile as wav
import soundfile
import os

for filename in os.listdir("."):
    if filename.endswith(".wav"):
    	data, samplerate = soundfile.read(filename)
    	print(data)
    	print(len(data))
    	soundfile.write("1.wav", data[samplerate*2:-1], samplerate, subtype='PCM_16')
    	# soundfile.write("1.wav", data[samplerate*2:], samplerate, subtype='PCM_16')
    	fs, signal = wav.read("1.wav")
    	print(fs)
    	print(signal)