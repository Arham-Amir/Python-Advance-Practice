def numToPowerN(num, n):
    if n == 1:
        return num
    return num * numToPowerN(num, n-1)


num = int(input("Enter the number: "))
pow = int(input("Enter the power: "))

if num == 0:
    print(f"{num} with power {pow} = 0")
elif pow == 0:
    print(f"{num} with power {pow} = 1")
elif pow>0:
    print(f"{num} with power {pow} = {numToPowerN(num, pow)}")
else:
    print(f"{num} with power {pow} = {1/numToPowerN(num, abs(pow))}")
    