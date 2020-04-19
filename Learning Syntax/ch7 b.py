
class Bird:
    count =0
    def __init__(self,chat):
        self.sound = chat
        Bird.count +=1
        
    def talk(self):
        return self.sound
        
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight =weight

#p1 = Person("John", 36)

p2= Person("Alex", 102, 70)
#print(p1.name)
#print(p1.age)
print(p2.name) 
print(p2.age)
print(p2.weight) 
       
        
        
        
        
        