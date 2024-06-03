number = 123456

def sumUptoN(num):
    if num < 10:
        return num
    
    sum = 0
    
    while num > 0:
        sum += num % 10
        num //= 10 
    return sumUptoN(sum)

print(sumUptoN(number))