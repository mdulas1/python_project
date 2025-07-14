class Bird:
    def __init__(self,name,color,legs,eyes):
        self.name = name
        self.color = color
        self.legs = legs
        self.eyes = eyes

a_Bird = Bird("eagle","black and white",2,2)
print(f"the {a_Bird.name} is looking {a_Bird.color} and has {a_Bird.legs} legs  and also has {a_Bird.eyes} eyes")
