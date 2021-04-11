letter = '''Dear <name>,
you are Selected!
Date : <date>
'''
name = input("Enter Your name:")
date = input("Enter date:")

letter = letter.replace("<name>",name)
letter = letter.replace("<date>", date)
print(letter)
