<<<<<<< HEAD
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
=======
class Word():

    def __init__(self):
        self.check_list = ['No Upper case letter in the Word','No Lower case letters in the word','No number at the last']
        self.upper = 0
        self.lower = 0
        self.digit = 0

    def check(self,word_input):

        if word_input[-1].isdigit():
            self.digit = 1

        for i in word_input:
            if i.isupper():
                self.upper = 1
                break

        for i in word_input:
            if i.islower():
                self.lower = 1
                break
        output = [self.upper,self.lower,self.digit]
        return output

    def validate(self,checked_list):
        key_list = []
        if all(checked_list):
            key_list = ['Perferct word']  
        else:
            # key_list = [key for key in range(0,len(checked_list)-1) if checked_list[key] == 0]
            key_list = [self.check_list[key] for key,value in enumerate(checked_list) if value == 0]
        return key_list

letter = Word()
print(letter.validate(letter.check('g@48')))
>>>>>>> 70ebef87f0d4fa43c18dd69c6b360775b5364eb2
