#Write a prime  generator program using only prime and using python loops

lower = int(input("Enter Lower Range Number: "))  
upper = int(input("Enter Upper Range Number: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  