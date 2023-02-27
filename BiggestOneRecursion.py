
def BiggestOneRecursion(x):
    global Biggest
    if(len(x) > 0):
        temp=x[0]
        if(temp>Biggest):
            Biggest=temp
        x.pop(0)
        BiggestOneRecursion(x)
    return Biggest

array = [4,5,243,43,555]
Biggest=array[0]
print(BiggestOneRecursion(array))
