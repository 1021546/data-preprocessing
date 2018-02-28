import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('10.wav')
frequencies, times, spectogram = signal.spectrogram(samples, sample_rate)

print(frequencies)
print(frequencies.shape)
print()
print(times)
print(times.shape)
print()
print(spectogram)
print(spectogram.shape)
print()

plt.imshow(spectogram)
plt.pcolormesh(times, frequencies, spectogram, cmap='RdBu')
plt.colorbar()
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
# plt.autoscale(enable=True, axis='x', tight=True)
# plt.autoscale(enable=True, axis='y', tight=True)
# plt.autoscale(enable=True, axis='both', tight=True)
plt.axis('tight')
plt.show()
