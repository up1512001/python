with open ('sample.txt','r') as f:
    text = f.read()
    text = text.replace('donkey','####')

with open('sample.txt','w') as f:
    f.write(text)

