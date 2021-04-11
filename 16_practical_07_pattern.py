n = int (input("Enter number: "))

for i in range(n):
    # for j in range(n-i-1):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))

