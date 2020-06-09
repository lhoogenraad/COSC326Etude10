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
	folders.append(files_on_level)
	folders[i].append(old_folder)
	i+=1
	return i

# extracts the number from the filename, uses it for sorting
def extract_number(filename):
	num_str = ""
	for char in filename:
		if(char in "0123456789"):
			num_str += char
	num = int(num_str)
	return num


# gonna try to get the directory inputted into something
input_dir = input("Enter Directory: ")
folders = []
file_names = []
all_dict = {}
folders = []
numbers = []

directory = os.scandir(input_dir)
find_files(directory, all_dict, file_names, folders, input_dir, 0)
#print(folders)
# Sort our array of filenames that we hopefully read in

i = 0
while i < len(file_names):
	numbers.append(extract_number(file_names[i]))
	file_names[i] = [file_names[i], numbers[i]]
	i+=1
numbers.sort()
file_names.sort()
print(numbers)
write_f = open('result.txt', 'w')
write_f.close()
write_f = open('result.txt', 'a')

i = 0
while i < len(numbers):
	for file in file_names:
		if(file[1] == numbers[i]):
			file_string = input_dir + '/' + file[0]
			try:
				read_f = open(file_string, 'r')
			except:
				j = 0
				while j < len(folders)-1:
					k = 0
					while k < len(folders[j])-1:
						if(file[0] == folders[j][k]):
							file_string = folders[j][len(folders[j])-1] + '/' + file[0]
							read_f = open(file_string, 'r')
							# adding breaks to make process more efficient
							break
						k+=1
					# break out of folders file loop if found file
					if not read_f.closed:
						break
					j+=1
			write_f.write(read_f.read())
			write_f.write('\n')
			read_f.close()
			# breaks out of file list if found
			break
	i+=1
write_f.close()
