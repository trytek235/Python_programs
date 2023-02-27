def summary(list):
    if(len(list)==1):
        return list[0]
    sum = list[0] + summary(list[1:])
    return sum

array = [2,53,42,43,45,234,421,31]
print(summary(array))