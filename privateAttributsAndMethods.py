class Student:
    def __init__(self, _name, _age):
        self.__name = _name
        self.__age = _age
        pass
    def __str__(self) -> str:
        return f"Student('{self.__name}, {self.__age}')"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def setName(self, _name):
       self.__name = _name

s = Student("Arham", 22)
print(s)
# s.name = "asd"    not allowed
s.setName = "asd"
print(s)