text = True
i =1 
with open('log.txt') as f:
    while text:
        text = f.readline().lower()
        #print(text)
        if 'python' in text:
            print("Present at "+str(i))
        i+=1
