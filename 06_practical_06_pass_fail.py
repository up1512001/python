sub1 = int(input("Enter Marks:"))
sub2 = int(input("Enter Marks:"))
sub3 = int(input("Enter Marks:"))

if(sub1<33 or sub2<33 or sub3 < 33):
    print("Fali...")
elif((sub1+sub2+sub3)/3 <40):
    print("You are fali")
else:
    print("Pass...")
