from pydub import AudioSegment
import scipy.io.wavfile as wav
import soundfile
import os

for filename in os.listdir("."):
    if filename.endswith(".wav"):
    	print(filename)
    	data, samplerate = soundfile.read(filename)
    	print(data)
    	print(len(data))
    	
    	t1 = 1 * 1000 #Works in milliseconds
    	# t2 = 2 * 1000
    	newAudio = AudioSegment.from_wav(filename)

    	newAudio1 = newAudio[t1:]

    	file_no_extension = os.path.splitext(filename)
    	temp_file = file_no_extension[0]+"_1"+file_no_extension[-1]

    	newAudio1.export(temp_file, format="wav") #Exports to a wav file in the current path.
    	fs, signal = wav.read(temp_file)
    	print(fs)
    	print(signal)