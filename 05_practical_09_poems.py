f = open('poems.txt')
text = f.read()
f.close()
# print(text)
if 'twinkle' in text:
    print('Present')
else:
    print("Not present")

