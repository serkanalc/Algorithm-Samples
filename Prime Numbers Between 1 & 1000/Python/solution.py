d = 1 
u = 1000 
  
for sayi in range(d,u + 1):  
   if num > 1:  
       for i in range(2,num/2):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
