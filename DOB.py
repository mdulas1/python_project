from datetime import datetime
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = int(dob)
        
    def calculateAge(self):
        current_year = datetime.now().year
        current_age = current_year - self.dob
        print(f"your current Age is {current_age}")
        
jibrin =Person("jibrin","Nigeria",2001)
jibrin.calculateAge()