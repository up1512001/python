b = set()
b.add(2)
b.add(4)
b.add(1)
b.add(5)
# b.add([2,3,4,5]) you can not add list in set or dictionary in set
b.add((3,4,5))

print(len(b))
b.remove(5)
# b.remove(15) throws error
print(b.pop())

print(b.union({2,4,5,6}))
print(b.intersection({1,2,4,5}))



print(b)