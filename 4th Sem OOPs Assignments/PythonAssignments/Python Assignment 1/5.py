#Write first seven Fibinacci numbers using generator next function/yield in python.Trace and memorize the function.

def fibo():
    a,b = 0,1
    for i in range(1,8):
        yield a
        a,b = b, a+b
for fib in fibo():
    print(fib)