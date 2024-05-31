def numToPowerN(num, n):
    if n == 0:
        return 1
    elif n%2==0:
        return numToPowerN(num*num, n//2)
    else:
        return num * numToPowerN(num*num, (n-1)//2)


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
    