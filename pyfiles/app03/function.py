from flask import Flask

class Word():

    def __init__(self):
        self.check_list = ['No Capital letter at the start','No symbols in the middle','No numbers at the last']

    def check(self,word_input):
        output = word_input + ' hello'
        return output

    
