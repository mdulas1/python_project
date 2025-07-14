class Nafisat:
    def __init__(self,name,age,gender,town,village):
        self.name =name
        self.age = age
        self.gender = gender
        self.town = town
        self.village = village

a_nafisat = Nafisat("nafisat hassan aliyu", 13, "female", "bauchi","souro")
print(f"my name is {a_nafisat.name} i am {a_nafisat.age} year old  a  {a_nafisat.gender} from {a_nafisat.village} in {a_nafisat.town} state")
