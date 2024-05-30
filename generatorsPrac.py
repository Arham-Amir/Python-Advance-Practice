import sys

def getNumbersMultipleOf10():
    num = 1
    while True:
        num*=10
        yield num
        
func = getNumbersMultipleOf10()      
print(next(func))
print(next(func))
print(next(func))

print(sys.getsizeof(getNumbersMultipleOf10))