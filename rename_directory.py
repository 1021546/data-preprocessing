import os

number = 31

for directory in os.listdir("."):
    if os.path.isdir(directory):   	
    	os.rename(directory, 'test'+str(number))
    	number+=1