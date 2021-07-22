#Filter out the odd squares using map,filter,list

arr = [num for num in range(1,100)]

filtereadArr = list(filter(lambda x: (x%2 == 1), arr))


myArr = list(map(lambda x: x*x, filtereadArr))


print(myArr)