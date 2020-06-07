from pathlib import Path
import os
# semi-recursive function to find all files in a directory
# just finding files, will parse and sort later
def find_files(dir, raw_files, content_array):
	for file in dir:
		if(os.path.isfile(file)):
			raw_files.append(file.name)
			#with open(os.path + file, 'r') as f:
			#	content_array.append(f.read())
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

	job_site = int(namesplit[0])
	lab_desk = int(namesplit[1])
	job_num = int(namesplit[2])

	# This code checks that the job numbers are in the valid range
	# Does not check that job_num increases in sequential order
	#todo: Account for leading 0 in numbers < 10 e.g. job_num should be 04, not 4
	#todo: probably need to do some bs string manipulation
	if job_site < 1 and job_site > 5:
		return False
	elif lab_desk < 1 and lab_desk > 25:
		return False
	elif job_num < 1 and job_num > 99:
		return False

	# This code accounts for when the number is between 1 and 9 inclusive, it checks that
	# the actual string has a leading 0
	if namesplit[0][0] != '0':
		return False
	elif lab_desk < 10 and namesplit[1][0] != '0':
		return False
	elif job_num < 10 and namesplit[2][0] != '0':
		return False

	if extension != ".txt":
		return False
	return True


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
for s in raw_files:
	print(s, "validity:", validate_filename(s))