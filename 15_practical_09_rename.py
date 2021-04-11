oldname = "another.txt"
newname = 'Renamed_by_pythoon.txt'

import os

with open(oldname) as f:
    text = f.read()
with open(newname,'w') as f:
    f.write(text)
os.remove(oldname)
