class University:
    uni_name = "UET Lahore"
    NumberOfStudents = 5000
    NumberOfDepartments = 30
    
    def __init__(self):
        pass
        
    @classmethod
    def classMethod(cls):
        print("Class:\t", cls)

    def instanceMethod(self):
        print("Instance:\t", self)

    @staticmethod
    def staticMethod():
        print("Static method:\t", University.uni_name)
     
    def __repr__(self):
        return f"University(uni_name={University.uni_name}, NumberOfStudents={University.NumberOfStudents}, NumberOfDepartments={University.NumberOfDepartments})"  


uni = University()

University.classMethod()
uni.instanceMethod()
University.staticMethod()