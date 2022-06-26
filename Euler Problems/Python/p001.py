for i in range(1,1000):
    rslt= sum(i for i in range (1000) if(i%5 == 0 or i%3 == 0))
print(rslt)
