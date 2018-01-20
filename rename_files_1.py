'''
import os
number = 0
for filename in os.listdir("./train1/"):
	path="./train1/"
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(path+filename, path+str(number)+'.wav')
		number+=1

number = 0
for filename in os.listdir("./train2/"):
	path="./train2/"
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(path+filename, path+str(number)+'.wav')
		number+=1

number = 0
for filename in os.listdir("./train3/"):
	path="./train3/"
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(path+filename, path+str(number)+'.wav')
		number+=1

number = 0
for filename in os.listdir("./train4/"):
	path="./train4/"
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(path+filename, path+str(number)+'.wav')
		number+=1

number = 0
for filename in os.listdir("./test/"):
	path="./test/"
	if filename.endswith(".wav"):
		# print(filename)
		os.rename(path+filename, path+str(number)+'.wav')
		number+=1
'''
		
import os

for directory in os.listdir("."):
    if os.path.isdir(directory):
    	number = 0
    	for filename in os.listdir(directory):
    		if filename.endswith(".wav"):
    			path=directory+"/"
    			os.rename(path+filename, path+str(number)+'.wav')
    			number+=1