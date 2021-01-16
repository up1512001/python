# basic code in python which return power of given base number
# using for loops and functions
# shows internal working of any default functions

def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(2,3))





