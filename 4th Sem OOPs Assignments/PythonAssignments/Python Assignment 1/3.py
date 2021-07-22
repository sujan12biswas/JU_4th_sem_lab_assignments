#Print first 10 odd and even numbers using iterator and compress. You can use duck typing
import itertools
import operator

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_select=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
even_select=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

odd=itertools.compress(numbers,odd_select)
even=itertools.compress(numbers,even_select)


print("Odd numbers :")
for i in odd:
    print(i,end=' ')
print("\nEven Number :")
for j in even:
    print(j,end=' ')