# use open function to read content of file
f= open('sample.txt','r') # by default mode is read (r)
data = f.read()
print(data)
# data = f.read(19)
# print(data) # first 19 of file
f.close()





