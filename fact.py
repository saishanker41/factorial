def factorial(num):
    
    if num < 0:
       return 0
    if num == 0:
       return 1
    fact = 1
    else:
        for i in range(1,num + 1):
            fact = fact * i
        return fact
        
        
