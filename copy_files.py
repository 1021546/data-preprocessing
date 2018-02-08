import os
import shutil

dstdir='./train49'
if not os.path.exists(dstdir):
	os.makedirs(dstdir) # create all directories, raise an error if it already exists

step=0
count=0
fileNum=49

for filename in os.listdir("."):
	if filename.endswith(".wav"):
		# print(filename)
		step+=1
		if step>30:
			if step%4:
				shutil.copy(filename, dstdir)
				count+=1
			if count==20:
				count=0
				fileNum+=1
				dstdir='./train'+str(fileNum)
				os.makedirs(dstdir) # create all directories, raise an error if it already exists

current_path=os.getcwd()
# C:\\Users\\cse_ncku\\Desktop\\five people\\s22
# current_path=os.path.dirname(os.path.abspath(__file__))
# C:\Users\cse_ncku\Desktop\five people\s22

# target_directory = current_path[-2:]

target_directory=current_path.split('\\')
# ['C:', 'Users', 'cse_ncku', 'Desktop', 'five people', 's22']

destination_path = "C:/Users/cse_ncku/Desktop/speaker_wav/"+target_directory[5][1:]

for directory in os.listdir("."):
    if os.path.isdir(directory):
    	shutil.move(directory,destination_path)
