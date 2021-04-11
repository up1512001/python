try:
    i = int(input('Enter number:'))
    i = 1/i
except Exception as e:
    print(e)
    exit()
# at any cost this will run even after {exit()} 
finally: 
    print('We Are Done...')

print('DONE>>>')