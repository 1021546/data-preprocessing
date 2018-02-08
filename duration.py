import wave
import contextlib
import os
import shutil

# min_duration = 100

# for directory in os.listdir("."):
#     if os.path.isdir(directory) and not directory=="__pycache__":
#         for filename in os.listdir(directory):
#             if filename.endswith(".wav"):
#                 pathFile=directory+"/"+filename
#                 f=wave.open(pathFile,'r')
#                 frames = f.getnframes()
#                 rate = f.getframerate()
#                 duration = frames / float(rate)
#                 print(pathFile)
#                 print(duration)
#                 if min_duration > duration:
#                     min_duration = duration
#                 f.close()
#                 if duration<1:
#                 	os.remove(pathFile)

# print('Minimum : %.4f' % min_duration)

for filename in os.listdir("."):
	if filename.endswith(".wav"):
		with contextlib.closing(wave.open(filename,'r')) as f:
			frames = f.getnframes()
			rate = f.getframerate()
			duration = frames / float(rate)
			print(filename)
			print(duration)
			f.close()
			if duration<1:
				os.remove(filename)


# for filename in os.listdir("."):
#     if filename.endswith(".wav"):
#         with contextlib.closing(wave.open(filename,'r')) as f:
#             frames = f.getnframes()
#             rate = f.getframerate()
#             duration = frames / float(rate)
#             if duration > 2:
#                 print(filename)
#                 print(duration)
#                 print()
#             f.close()

# for directory in os.listdir("."):
#     if os.path.isdir(directory) and not directory=="__pycache__":
#         for filename in os.listdir(directory):
#             if filename.endswith(".wav"):
#                 pathFile=directory+"/"+filename
#                 f=wave.open(pathFile,'r')
#                 frames = f.getnframes()
#                 rate = f.getframerate()
#                 duration = frames / float(rate)
#                 print(pathFile)
#                 print(duration)
#                 f.close()

dstdir='./temp'
if not os.path.exists(dstdir):
    os.makedirs(dstdir)

number = 0

for filename in os.listdir("."):
    if filename.endswith(".wav"):
        with contextlib.closing(wave.open(filename,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration > 2:
                number+=1
                print(str(number))
                print(filename)
                print(duration)
                print()
                shutil.copy(filename, dstdir)
            f.close()
