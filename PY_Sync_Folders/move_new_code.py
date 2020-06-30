#Script to synchronise contents of two folders based on extension
#Use case: Syncing Dev and Repository folders in local system before pushing Repo to git

import os,shutil,sys

# source_dir_str = "C:/Users/rumitra/Desktop/CPP/"
# target_dir_str = "C:/Personal/Codes/Github/Programming101_CPP/"
# ext_list = ["cpp"]

#args check
len_args = len(sys.argv)

if len_args!=4:
    print("Please provide valid arguments.")
    print("Arguments should be: source path, destination path, extensions (seperated by commas)")
    sys.exit()

#Get cmd arguments
source_dir_str = sys.argv[1].strip()
target_dir_str = sys.argv[2].strip()
ext_list = [i.strip().lower() for i in sys.argv[3].split(",")]

#Get all files
fileList_source_list = os.listdir(source_dir_str)
fileList_target_list = os.listdir(target_dir_str)

#init counters
move_count = 0
refreshed_count = 0

for filename in fileList_source_list:
    ext = filename.split(".")[-1]
    if filename not in fileList_target_list and ext in ext_list:
        shutil.copy2(source_dir_str+filename, target_dir_str)
        move_count+=1
        print("Added: "+filename)
    elif filename in fileList_target_list and ext in ext_list:
        shutil.copy2(source_dir_str+filename, target_dir_str) #Overwrites files if exist
        refreshed_count+=1

print("*** SUMMARY ***")
print("New files added: "+str(move_count))
print("Old files refreshed: "+str(refreshed_count))