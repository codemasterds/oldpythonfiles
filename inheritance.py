#single level inheritance
print(int(1))
class animal:
    def eating(self):
        print("dog is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")

obj=dog()
obj.eating()

obj.bark()
#mutli level inheritance        
print(int(2))
class animal:
    def eating(self):
        print("dog is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
class babydog(dog):
    def beep(self):
        print("dog i sbeeping")

obj=babydog()
obj.eating()

obj.bark()
           
obj.beep()
# heriracial level inhertiance
print(3)
class animal:
    def eating(self):
        print("dog is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
class babydog(dog):
    def beep(animal):
        print("dog i sbeeping")
        

obj=babydog()
obj.eating()

obj.bark()
           
obj.beep()
# mutli level inheritance
print(4)

class animal:
    def eating(self):
        print("dog is eating")
class dog:
    def bark(self):
        print("dog is barking")
class babydog(animal,dog):
    def beep(self):
        print("dog i sbeeping")
        

obj=babydog()
obj.eating()

obj.bark()
obj.beep()         
