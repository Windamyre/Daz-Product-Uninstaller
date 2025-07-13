import argparse
import os.path
import os.path
import os.path
from pdb import find_function
import zipfile
import os
import shutil

def main():
	#Set-up command line parser
	parser = argparse.ArgumentParser(description="removes files from a Daz Studio library")
	parser.add_argument("Zip",help="The name of the zip file.  Must be unencrypted")
	parser.add_argument("Library",help="Path to the Daz Studio Library to be affected")
	parser.add_argument("Dest",help="If no path provided, file will be deleted")
	parser.add_argument("-s", "--silent", action='store_true',help="set to True to suppress output")


	myArgs = parser.parse_args()
	trun_location=0
	count_moved =0
	count_skipped=0

	print("Starting....")
	
	files_to_remove = []
	# Get list of files in zip file
	if not os.path.exists(myArgs.Zip):
		print (f"File {myArgs.Zip} does not exist")
		quit()

	if not os.path.exists(myArgs.Library):
		print (f"Directory {myArgs.Library} does not exist.")
		quit()

	if not os.path.exists(myArgs.Dest):
		print(f"Directory {myArgs.Dest} does not exist.")
		quit()

	with zipfile.ZipFile(myArgs.Zip, 'r') as zip_file:
		file_list=zip_file.namelist()
		#print(file_list)
		for info in zip_file.infolist():
				if not info.is_dir():
					files_to_remove.append(info.filename)

	# Find where the path of the files begin by finding the first file that has 'data', 'runtime' or 'people' in it
	for file_name in files_to_remove:
		location = find_first_match(file_name,["data","Data","Runtime","runtime","People"])
		if location:
			trun_location = location[1]-1
			break

	# Modify the List to remove the leading information
	for i in range(len(files_to_remove)):
		files_to_remove[i] = files_to_remove[i][trun_location:]

	#move the files to the destination
	for file_to_move in files_to_remove:
		#Generate file paths
		Source_File = myArgs.Library.replace("\\","/") +file_to_move
		Dest_Path = myArgs.Dest.replace("\\","/") + os.path.dirname(file_to_move) +"/"
		
		try:
			#Create new directory if needed
			os.makedirs(Dest_Path,exist_ok=True)
			if not os.path.exists(Dest_Path + os.path.basename(file_to_move)):
				shutil.move(Source_File,Dest_Path)
				count_moved += 1
			else:
				print( f"File already exists - {Dest_Path}")
				count_skipped += 1
			if True: #not myArgs.Silent:
				print (f"Moved {Source_File} to {Dest_Path}.")
		except FileNotFoundError:
			print(f"File Not Found - {file_to_move}")
		except FileExistsError:
			print(f"File already moved - {file_to_move}")
		except Exception as e:
			print (f"Unplanned Error {e} ")

	print (f"Completed.  {count_moved} files moved, {count_skipped} skipped.")
1

"""  Not used
def find_file (root_folder, target_file):
	filename = os.path.basename(target_file)

	matches = []
	for dirpath,_,files in os.walk(root_folder):
		if filename in files:
			full_path= os.path.join(dirpath,filename)
			matches.append(full_path)
	return matches
"""

def find_first_match(haystack, needles):
    matches = [(needle, haystack.find(needle)) for needle in needles if haystack.find(needle) != -1]
    if matches:
        return min(matches, key=lambda x: x[1])  # (needle, index) with smallest index
    return None

if __name__ == "__main__":
	main()


