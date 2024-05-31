from collections import OrderedDict

d = OrderedDict()
d['b']= 2
d['a']= 5
d['c']= 4

for i in d.items():
    print(i)
    
# Maintain the order in which you add values