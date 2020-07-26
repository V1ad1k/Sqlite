
def calc(z):
    sum1 = 0
    sum2 = 0
    for i in range(1,z+1):
        sum1 += i
    sum1 = sum1**2
    for i in range(1,z+1):
        sum2 += i*i
    result = sum1 - sum2
    return result
print(calc(100))