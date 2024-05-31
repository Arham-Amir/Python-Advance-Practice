from enum import Enum, auto

class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

print(Weekday.MONDAY) 
print(Weekday.MONDAY.value) 

for day in Weekday:
    print(day)

print(Weekday.MONDAY in Weekday) 
print(1 in Weekday) 

print(Weekday(1)) 
