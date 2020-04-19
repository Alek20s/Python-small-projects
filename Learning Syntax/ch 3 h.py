i=1
for i in range(1,6):
     for j in range(1,6):
        if i ==1 and j==1:
            print ('Continue inner loop at i=1 j=1')
            continue
        if (i==2  and  j==1):             
            print ('Breaks inner loop at i=3, j=2')
            break    
        print ('Running i=', i, 'j=', j) 
        
        
        
        