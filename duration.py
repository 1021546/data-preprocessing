import wave
import contextlib
import os

for directory in os.listdir("."):
    if os.path.isdir(directory) and not directory=="__pycache__":
        for filename in os.listdir(directory):
            if filename.endswith(".wav"):
                pathFile=directory+"/"+filename
                f=wave.open(pathFile,'r')
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(pathFile)
                print(duration)
                f.close()
                if duration<1:
                	os.remove(pathFile)


# for filename in os.listdir("."):
# 	if filename.endswith(".wav"):
# 		with contextlib.closing(wave.open(filename,'r')) as f:
# 			frames = f.getnframes()
# 			rate = f.getframerate()
# 			duration = frames / float(rate)
# 			print(filename)
# 			print(duration)
# 			f.close()
# 			if duration<1:
# 				os.remove(filename)