import os
number = 0
for filename in os.listdir("."):
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(filename, str(number)+'.wav')
		number+=1