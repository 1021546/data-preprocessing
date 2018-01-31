import os
import shutil

dstdir='./train9'
if not os.path.exists(dstdir):
	os.makedirs(dstdir) # create all directories, raise an error if it already exists

step=0
count=0
fileNum=9

for filename in os.listdir("."):
	if filename.endswith(".wav"):
		# print(filename)
		step+=1
		if step>16:
			if not step%9:
				shutil.copy(filename, dstdir)
				count+=1
			if count==20:
				count=0
				fileNum+=1
				dstdir='./train'+str(fileNum)
				os.makedirs(dstdir) # create all directories, raise an error if it already exists