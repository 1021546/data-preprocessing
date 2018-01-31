import os
import shutil

# directory="./s35/"
# if not os.path.exists(directory):
#     os.makedirs(directory)
#     for filename in os.listdir("."):
#     	if filename[0:5]=="F1130":
#     		shutil.move(filename, directory+filename)


dir_num=36
pre_filename="F1131"
directory="./s"+str(dir_num)+"/"
if not os.path.exists(directory):
	os.makedirs(directory)
	for filename in os.listdir("."):
		if filename.endswith(".wav"):
			if filename[0:5]!=pre_filename: # if not filename[0:5]==pre_filename:
				pre_filename=filename[0:5]
				dir_num+=1
				directory="./s"+str(dir_num)+"/"
				os.makedirs(directory)
			shutil.move(filename, directory+filename)