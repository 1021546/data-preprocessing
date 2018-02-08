import os

for directory in os.listdir("."):
    if os.path.isdir(directory) and not os.listdir(directory):
    	if directory[0:4]=="test":
    		dir_num = int(directory[4:])
    	elif directory[0:5]=="train":
    		dir_num = int(directory[5:])
    	print(dir_num)
    	if dir_num > 50:
    		os.rmdir(directory)