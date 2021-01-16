# try Except
#
#
#value = 10/0
# if user will enter character or special symbol then ppython will show error
# to avoid that error
try:
  #  value = 10 / 0
    num = int(input("Enter Number:"))
    print(num)
# except will catch any error occurs in program like 10/0 is math error but it will show invalid input
# so we can catch specific type of error
# you can store error as value like below
except ZeroDivisionError as err:
    print(err)
except ValueError as v: # except ValueError:
    print(v)            # print("Invalid value")


