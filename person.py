#______________________person__________________#
class Person:
    def __init__(self, name, age, hand, leg):
        self.name = name
        self.age = age
        self.hand = hand
        self.leg = leg

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old. I have {self.hand} and {self.leg}."

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

#______________end of class________________#

a_person = Person("Jibrin", 25, 'two hands', 'two legs')
print(a_person.introduce())
print(a_person.celebrate_birthday())
print(a_person.introduce())