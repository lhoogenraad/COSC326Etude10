from pathlib import Path
import os
# semi-recursive function to find all files in a directory
# just finding files, will parse and sort later
def find_files(dir, dict, filenames, folders, old_folder, i):
	files_on_level = []
	for file in dir:
		if(os.path.isfile(file)):
			file_names.append(file.name)
			files_on_level.append(file.name)
			with open(file, 'r') as f:
				dict[file.name] = f.read()
		else:
			# must be a folder
			new_dir = os.scandir(file)
			new_folder = old_folder + '/' + file.name
			# open the folder and extract all files
			#folders.append(files_on_level)
			i = find_files(new_dir, all_dict, filenames, folders, new_folder, i)
	print(i)
	print(old_folder)
	folders.append(files_on_level)
	folders[i].append(old_folder)
	i+=1
	return i


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
	if job_site < 1 or job_site > 5:
		return False
	elif lab_desk < 1 or lab_desk > 25:
		return False
	elif job_num < 1 or job_num > 99:
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
folders = []
file_names = []
all_dict = {}
folders = []

directory = os.scandir(input_dir)
find_files(directory, all_dict, file_names, folders, input_dir, 0)
print(folders)
# Sort our array of filenames that we hopefully read in
file_names.sort()

# From here we've read in all our data, and are ready to manipulate it:

# These arrays contain valid files and their corresponding input
valid_files = []
valid_content = []
# The same but for invalid files and their corresponding input
invalid_files = []
invalid_content = []


for i in range(len(file_names)):
	# If our current file has a valid name, add it to our valid files array
	# and add the corresponding content to the valid files array
	if validate_filename(file_names[i]):
		valid_files.append(file_names[i])
		valid_content.append(all_dict[file_names[i]])
	else:
		# If we end up here, our filename is not valid, so add the filename and its contents to
		# corresponding invalid arrays
		invalid_files.append(file_names[i])
		invalid_content.append(all_dict[file_names[i]])


for s in sorted(all_dict.keys()):
	#print(s, "validity:", validate_filename(s))
	pass
# basic idea behind reading files
#read_f = open('BaseCase/03-05-01.txt', 'r')
#print(read_f.read())
#read_f.close()
write_f = open('result.txt', 'w')
write_f.close()
write_f = open('result.txt', 'a')
for file in valid_files:
	file_string = input_dir + '/' + file
	try:
		read_f = open(file_string, 'r')
	except:
		# if it fails, means the file isn't in the folder, 
		# so look through the other folders
		i = 0
		# folders[len-1] = base level
		while i < len(folders)-1:
			j = 0
			# last item is the folder
			while j < len(folders[i])-1:
				if(file == folders[i][j]):
					file_string = folders[i][len(folders[i])-1] + '/' + file
					read_f = open(file_string, 'r')
				j+=1
			i+=1
	
	
	write_f.write(read_f.read())
	print(read_f.read())
	write_f.write('\n')
	read_f.close()
write_f.close()