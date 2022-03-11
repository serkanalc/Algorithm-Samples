d = 1 
u = 1000 
  
for num in range(d,u + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
