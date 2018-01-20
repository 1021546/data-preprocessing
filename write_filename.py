import os

text_file = open("Output.txt", "w")
for directory in os.listdir("."):
	if os.path.isdir(directory):
		for filename in os.listdir(directory):
			if filename.endswith(".wav"):
				text_file.write(filename+"\n")
text_file.close()