al ='Gokul@48'
print(al[0].isupper())
print(al[-1].isdigit())

uppercase = False
lowercase = False
while lowercase and uppercase:
    for i in al:
        if i.isupper():
            uppercase = True
        elif i.islower():
            lowercase = True
    