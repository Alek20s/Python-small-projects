import numpy as np
x1 = np.loadtxt('data1.txt', skiprows=1, unpack=True, dtype=np.str)
w= 'coronvirus'
j=1
while j<2990:
    j=j+1
    b= x1[j]
#    print (b,len(b), b[0])
    
    v=b
    k=0
    while k<len(v):
        a= (v[k] in w)
        k=k+1
        if a == True:
            if k==len(v):
                print (v)
        elif a != True:
#            print('not that word')
            break