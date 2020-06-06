from pathlib import Path
import os

# gonna try to get the directory inputted into something
input_dir = input("Enter Directory: ");
print(input_dir);

directory = os.scandir(input_dir);
for file in directory:
	print(file.name);
