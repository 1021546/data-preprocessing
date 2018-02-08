import os
import shutil

for directory in os.listdir("."):
    if os.path.isdir(directory):
    	shutil.move(directory,"C:/Users/cse_ncku/Desktop/speaker_wav/22")