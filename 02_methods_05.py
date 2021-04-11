myDir = {
    "fast": "Quick",
    "Utsav": "Richest Person",
    "marks": [2, 3, 4],
    "second": {'hello': 'how are you', 'bye': 'see you soon'},
    1:30
}

print(myDir.keys())
print(type(myDir))
print(myDir.values())
print(myDir.items())
print(type(myDir.items()))
upd = {
    2:"hjdwh",
    4:"ksjfw"
}
print(myDir.update(upd))
print(myDir)

print(myDir.get("Utsav")) # returns none if key is not present 
# print(myDir['Utsav1']) # throws error if key is not present in dictionary
