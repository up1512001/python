with open('sample.txt') as f:
    text = f.read()

word = ['donkey','hello','buy']

for i in word:
    text = text.replace(i,'$%^$%^')

with open ('sample.txt','w') as f:
    f.write(text)
