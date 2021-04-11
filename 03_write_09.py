# is that file dosen't exists then it will create that file 
# and if already created it dosen't matter it will over write
f = open('another.txt','w')
f.write("Hello utsav patel")
f.close()
# appends content to end of that previously created file
# or if not resent then it will create that file
f= open('another.txt','a')
f.write("\nHow are You?")
f.close()
