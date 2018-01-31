import os

for dirname, dirnames, filenames in os.walk('.'):
	print(dirname)
	print(dirnames)
	print(filenames)