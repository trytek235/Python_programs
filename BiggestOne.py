def theBiggestOne(x):
    Biggest = 0
    for i in x:
        if(x.index(i)-1==0):
            Biggest = x[0]
        else:
            if(Biggest<x[x.index(i)]):
                Biggest = x[x.index(i)]
    return Biggest
        #print(x.index(i))
array = [4,5,243,43] 
print(theBiggestOne(array))
