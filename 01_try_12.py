

while True:
    print('Enter Q for EXIT')
    a = input('enter number:')
    if a=='q':
        break
    try:
        print('Trying...')
        a = int(a)
        if a > 6:
            print('Number Greter then 6...')
    except Exception as e:
        print(f'your input result in error {e}')

print('GAME OVER')
