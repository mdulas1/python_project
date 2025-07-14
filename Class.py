class My_car():
    def __init__(self,parameter1,parameter2):

        self.property1 = parameter1
        self.property2 = parameter2
    
    def drive(self):
        x = self.property1 + self.property2

        print('the  speed of the car',str(x), 'km/h')


car= My_car(100,40)
car.drive()
        
    