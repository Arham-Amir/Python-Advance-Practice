decimal_number = 20 

def getBinaryofDecimal(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num //= 2
    print(binary[::-1])
    
getBinaryofDecimal(decimal_number)