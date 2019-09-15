import os
import pprint
import sys

path = input(" Please enter the directory Name: ")
if os.path.exists:
    list_files_dir = os.listdir(path)
else:
    pprint.pprint("Please enter a valid path")
    sys.exit()

# pprint.pprint(list_files_dir)
list_files = []
list_dir = []

for files in list_files_dir:
    p = os.path.join(path,files)
    if os.path.isfile(p):
        list_files.append(p)
    else: 
        list_dir.append(p)

pprint.pprint(list_dir)
pprint.pprint(list_files)

# pprint.pprint(list_dir,list_files)
