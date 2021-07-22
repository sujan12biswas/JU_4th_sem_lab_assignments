#Write a code which yields all terms of the geometric progression a,aq,aq2,aq3...
#when the progression produess a term that is greater than 100000,the generator stop with a return statement.

def generateGP(a, r):
    print("\n")
    for i in range(0, 100000):
        current = a*pow(r,i)
        if current > 100000:
            return
        print(current, end=" ")
a = 1
r = 3

generateGP(a, r)
print("\n")