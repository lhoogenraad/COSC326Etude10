from pathlib import Path
import os
# semi-recursive function to find all files in a directory
# just finding files, will parse and sort later
def find_files(dir, raw_files, content_array):
	for file in dir:
		if(os.path.isfile(file)):
			raw_files.append(file.name)
			with open(os.path + file, 'r') as f:
				content_array.append(f.read())
		else:
			# must be a folder
			new_dir = os.scandir(file)
			# open the folder and extract all files
			find_files(new_dir, raw_files, content_array)
	return


# This function will return true if file is valid, false if invalid
def validate_filename(filename):
	name = filename[:-4]
	extension = filename[-4:]
	namesplit = name.split("-")

	# Checking the name of the file is split into 3 sections
	if len(namesplit) != 3:
		return False
	# Checking all sections of the filename are numerical
	for s in namesplit:
		if not s.isnumeric():
			return False

	if extension != ".txt":
		return False


# gonna try to get the directory inputted into something
input_dir = input("Enter Directory: ")
print(input_dir)
raw_files = []
folders = []
contents = []

directory = os.scandir(input_dir)
find_files(directory, raw_files, contents)


print("unsorted:", raw_files)
raw_files.sort()
print("sorted:", raw_files)

#print(contents)