#Create a list of all the number up to N=50 which are multiples of five using anonymous function
myL = []
def myd(x, y): return (x % y == 0)



for i in range(1,51):
    if myd(i, 5):
        myL.append(i)

print(myL)
