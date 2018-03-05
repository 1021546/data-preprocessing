import scipy.io.wavfile as wav
import numpy as np
file_name_1 ="0.wav"
file_name_2 ="1.wav"

fs_1, signal_1 = wav.read(file_name_1)

fs_2, signal_2 = wav.read(file_name_2)
# print(type(signal_1))
# print(signal_1.shape)
# print(signal_1)
# print(type(signal_2))
# print(signal_2.shape)
# print(signal_2)
concatenate_wav = np.hstack((signal_1,signal_2))
# print(type(concatenate_wav))
# print(concatenate_wav.shape)
# print(concatenate_wav)

wav.write("output.wav",fs_1,concatenate_wav)