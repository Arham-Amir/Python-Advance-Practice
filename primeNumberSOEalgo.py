import math 
import functools
n = 3

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

def primeUptoN(n):
    if n <= 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for num in range(2, int(math.sqrt(n)) + 1):
        if isPrime(num):
            for i in range(num*num, n, num):
                primes[i] = False
    print("Number Of Primes: ", sum(primes))
    return primes
    
    

for index, prime in enumerate(primeUptoN(n)):
    print(index, prime)