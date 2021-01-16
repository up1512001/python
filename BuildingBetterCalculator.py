#
#
#


num1 =float(input("Enter First number:"))
op =input("Enter Operator:")
num2 =float(input("Enter Second number:"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")