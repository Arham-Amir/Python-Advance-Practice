def numToPowerN(num, n):
    result = 1
    while n>0:
        if n % 2 == 1:
            result *= num
        num *= num
        n //=2
    print(result)


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
    