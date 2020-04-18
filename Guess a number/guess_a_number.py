import numpy as np
x = np.random.randint(100, size=1)

y=999
while x  != y:
        
        y =int( input(" enter a number between 1 and 100:     "))
        print (y)

        if x>y:
                print ("too small, try again.")

        if x<y:
                print ("too big, try again.")
        
print ("well done, you guess,it is", int(x))
