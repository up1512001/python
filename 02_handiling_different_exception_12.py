try:
    a = int(input('Enter Number:'))
    c = 1/a
except ValueError as e:
    # print(f'Exception1 Occured {e}')
    print('Please Enter Valid Value...')
except ZeroDivisionError as e:
    # print(f'Exception2 Occured {e}')
    print('Make sure you are not dividing by ZERO...')
# except Exception as e:
#     print(f'Excption3 Occured is {e}')

print('Thanks for using ...')