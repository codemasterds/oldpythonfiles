class details:
    """ this is document about employee"""

    def __init__(self,name,addr,sal):
                 self.name=name
                 self.addr=addr
                 self.sal=sal
    def info(self):
        print("the name of employee is",self.name)
        print("the addr of the eemp is",self.addr)
        print("the sal of the emp is",self.sal)

print(details.__doc__)
t=details("sai","wgl",100000)
t.info()
         

help(details)
