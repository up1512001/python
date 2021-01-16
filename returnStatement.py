# using return keyword
# if you don't write return then like val*val*val None will be the output when we print the cube(4)
# so return  statement is useful in this type of situation
# it can return any data type premitive or non premitive
# you can also store return value
# after return statement any code further that will not executed
def cube(val):
   # val*val*val
    return pow(val,3)
    # like this
    # print("hello")
result = cube(5)
print(result)



