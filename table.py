class Employee:
    def __init__(self,name, employeeID,salary):
        self._name = name
        self._employeeID = employeeID
        self.__salary = salary
        
        
    def getName(self):
        print("The name of employee:{self._name}")
        
        
        
    def getSalary(self):
        print(f"the salary of employee is:{self.__salary}")
        
        
    def getEmployeeID(self):
        print(f"the employeeID:{self._employeeID}")
        
Employee1 = Employee(f"tanimu maawiya jibrin", 1084823, "$200")

Employee1.getName()

Employee1.getEmployeeID()

Employee1.getSalary()