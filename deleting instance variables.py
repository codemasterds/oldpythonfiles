class test1:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def delete(self):
        del self.x
p=test1(1,2,3)
p.delete()
print(p.__dict__)

        
