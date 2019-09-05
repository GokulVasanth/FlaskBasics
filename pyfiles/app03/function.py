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