#Python3 code for k largest elements in an array

def kLargest(arr, k):
	
	listA.sort(reverse = True)
	for i in range(k):
		print (arr[i], end =" ")
listA = []
n = int(input ("Enter Number of elements in this list: "))
for i in range(0,n):
    print("Emter element  no-{}: ".format(i+1))
    elm = int(input())
    listA.append(elm)
print(listA)
k = int(input("How many number of output: "))

kLargest(listA, k)
