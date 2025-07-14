class Travel:
    def __init__(self,country, month,type):
        self.country = country
        self.month = month
        self.type = type
        self.price = 0

    def trip_info (self):
        if self.month >= 10 and self.month <=3:
             print(f"you are going to {self.country} int the winetr this is {self.type} trip")
        elif self.month  > 3 and self.month > 10:
            print(f"you are going to {self.country} in the summer this is {self.type} trip" )
        else:
            print("invalid input")

    def calc_cost(self,cost):
        while cost !=0:


         cost = []
         self.price += cost
         cost.append(cost)
        
         cost = int(input("enter another cost"))
    def Advice(self,num):
        if num < 500:
            print("low budget")
        elif num >= 500 and num < 1500:
            print("take a flight to anywhere")
