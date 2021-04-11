my = {
    'pankha':'fan',
    'dabba':'box',
    'hath':'hand',
    'mathu':'head'
}
print("Options are",my.keys())
a = input("Enter Hindi word\n")
# print("Meaning of word",my[a]) # throws error if key is not present
print("Meaning of word", my.get(a))
