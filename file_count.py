import os, os.path


# simple version for working with CWD
# for directory in os.listdir("."):
#     if os.path.isdir(directory):
#     	print(directory)
#     	fileCount = len([filename for filename in os.listdir(directory) if filename.endswith(".wav")])
#     	print(fileCount)



# totalFile = 0

# simple version for working with CWD
# for directory in os.listdir("."):
#     if os.path.isdir(directory):
#     	print(directory)
#     	fileCount = len([filename for filename in os.listdir(directory) if filename.endswith(".wav")])
#     	print(fileCount)
    	# totalFile += fileCount

# print(totalFile)


for directory in os.listdir("."):
    if os.path.isdir(directory):
    	fileCount = len([filename for filename in os.listdir(directory) if filename.endswith(".wav")])
    	if fileCount != 20:
    		print(directory)
    		print(fileCount)
