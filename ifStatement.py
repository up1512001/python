# in if condition put your condition after if and at end of condition put colen
# you can put as much code you want in side if or else statement

# and or are keyword to check more than one condition

# in 'and' every condition must be true to executed after lines in if or elif
# in 'or' only one codition needs to be true to execute

is_male =False
is_tall =False
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("You are short male")
elif not is_male and is_tall:
    print("You are tall but not male")
else:
    print("Yor are not male and not tall")
