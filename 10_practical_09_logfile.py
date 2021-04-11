with open('log.txt') as f:
    text = f.read().lower()

if 'python' in text:
    print("present")
else:
    print('Not present')
