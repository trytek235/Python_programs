def sumRec(x):
    if(len(x) == 0):
        sum = 0
    else:
        temp = x[0]
        x.pop(0)
        sum=temp + sumRec(x)
    return sum

array = [4,5,243,43]
print(sumRec(array))
