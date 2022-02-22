class test:
    def __init__(self,x,y):
        print("constuctor is created")
        self.x=x
        self.y=y
    def display(self):
        print("x=",self.x)
        print("y=",self.y)
t=test(10,20)
t.display()
t.y=30
t.display()
print(t.x,t.y)
