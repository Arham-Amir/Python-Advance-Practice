from enum import Enum
class fool(Enum):
    EVEN = 0
    ODD = 1

a = 5
b = 2

print(a & b) 
print(a | b) 
print(a ^ b) 
print(~a)    
print(a << 1)
print(a >> 1)


print(f"{a} is odd: {fool(a&1).name}")
print(f"{b} is odd: {fool(b&1).name}")
