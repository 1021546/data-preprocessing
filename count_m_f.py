import os

M = 0
F = 0
S = 0

for directory in os.listdir("."):
    if os.path.isdir(directory):
    	filenames = os.listdir(directory)
    	if len(filenames) != 0:
	    	first_filename = filenames[0]
	    	gender = first_filename[0]
	    	if gender == 'M':
	    		M += 1
	    	elif gender == 'F':
	    		F += 1
	    	else:
	    		S += 1

print("M: ",M)
print("F: ",F)
print("S: ",S)