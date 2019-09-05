# from flask import Flask

class Word():

    def __init__(self):
        self.check_list = ['No Capital letter at the start','No symbols in the middle','No numbers at the last']
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

letter = Word()
print(letter.check('goku'))