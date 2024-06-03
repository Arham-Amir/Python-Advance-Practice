a = 4
b = 2
c = 3
f_max = float('-inf')
s_max = float('-inf')
for i in [a, b, c]:
    if i >= f_max:
        s_max = f_max
        f_max = i
    elif i> s_max:
        s_max = i
print("FirstMax = ", f_max)    
print("SecondMax = ", s_max)    