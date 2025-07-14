import random
random.seed(0)

class X:
    def __init__(self,arr):
        self.arr = arr
        def get_num(self,i):
            return self.arr[i]
        def __call__(self):
            return self.arr
        
xobj = X( random.sample(range(1,10), 5) ) ## (A)
print(xobj.get_num(2)) # 1 ## (B)
print(xobj()) # [7, 9, 1, 3, 5] ## (C)
xobj = X( random.sample(range(1,10), 5) ) ## (D)
print(xobj.get_num(2)) # 9 ## (E)
print(xobj()) # [8, 7, 9, 3, 4] ##

