def prime(n):
      if n>1:
            for i in range(2,n):
                  if(n%i==0):
                      return False

            return True
            
                      
      
def num(p):
      for x in range(2,p+1):
            
      
        if  prime(x) :
            print(x)
num(10)
            

