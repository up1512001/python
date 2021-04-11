comment = input("Enter text")
spam = False

if("make a lot of money" in comment):
    spam=True
elif ("buy now" in comment):
    spam = True
elif("click this" in comment):
    spam = True

if(spam):
    print("Spam text")
else:
    print("Not spam")



