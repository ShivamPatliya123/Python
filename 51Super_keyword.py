class first:
    def add(self,a,b):
        c=a+b
        print(c)
    def sub(self,a,b):
        c=a-b
        print("hey")
        print(c)

class second(first):
    def sub(self,a,b):
        super().sub(a,b)
    def multiply(self,a,b):
        c=a*b 
        print(c)

obj=first()
obj.add(8,2)
obj.sub(6,4)

obj1=second()
obj1.multiply(6,7)
obj1.sub(57,8)

