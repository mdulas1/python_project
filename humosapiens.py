
class Bird:
      # class attribute
      sepecies1 = "has"
      sepecies2 = "domestic bird"

      def __init__(self,name, legs,fly):
            self.name = name
            self.legs= legs
            self.fly = fly

x = Bird( "eagle", "two legs", "can fly")

print(x.name,x.sepecies1,x.legs,x.fly)
            