# ITERATIVE APPROACH

# def fact(n):
#     pro = 1
#     for i in range(n):
#         pro = pro * (i+1)
#     return pro

# print(fact(7))
# fa = 1
# n = 4
# for i in range(n):
#     fa = fa * (i+1)

# print(fa)

# RECURSIVE APPROACH
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return fact(n-1)*n

print(fact(5))

