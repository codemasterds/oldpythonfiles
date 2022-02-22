class test:
    x=10
    def __init__(self):
        test.x=20
        
    def met(self):
        print(self.x)
        print(test.x)
p=test()
print(p.x)
p.met()
p.x=30
print(p.x)
