file1 = 'copy.txt'
file2 = 'this.txt'

with open(file1,'rt') as f:
    text1 = f.read()
with open(file2,'rt') as f:
    text2 = f.read()

if text1 == text2:
    print("COPYED...")
else:
    print("DIFFERENT...")
