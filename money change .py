


Sum = int(input('enter thr sum of coins'))#sum of which changes are required
change =[1,2,5,10,20,50,100,200,500,2000]    #changes you have 
l2=[]                                    


while Sum>0:
    for i in change:
        if i<=Sum :
            l2.append(i)


    print(l2[-1])                       ##actual change           
    Sum=Sum-l2[-1]
    
    
    
        
   


    
                     

