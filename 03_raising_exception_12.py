def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError('This is not good-UT')

b = increment('49r')
print(b)