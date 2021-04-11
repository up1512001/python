# STRIP USE
this = "     utsav is good boy"
# print(this)
# print(this.strip())

def remove_split(string,word):
    newStr = string.replace(word,"XYZ")
    return newStr.strip()
p = remove_split(this,'utsav')
print(p)


