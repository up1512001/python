def pat(n):
    if n==0:
        return 
    print("*"*(n))
    pat(n-1)
n = int(input("Enter Number: "))
print(pat(n))
