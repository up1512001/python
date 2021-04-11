def mulTable(n,i=1):
    print(f"{n} X {i} = {n*i}")
    if i ==10:
        return 
    else:
        return mulTable(n,i+1)

mulTable(20)
