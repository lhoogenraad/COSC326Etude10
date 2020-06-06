from pathlib import Path
import os
# semi-recursive function to find all files in a directory
# just finding files, will parse and sort later
def find_files(dir, raw_files):
	for file in dir:
		if(os.path.isfile(file)):
			raw_files.append(file);
		else:
			# must be a folder
			new_dir = os.scandir(file.name);
			print(new_dir);

# gonna try to get the directory inputted into something
input_dir = input("Enter Directory: ");
print(input_dir);
raw_files = []
folders = []

directory = os.scandir(input_dir);
find_files(directory, raw_files);



