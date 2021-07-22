#Write a discount coupon code using dictionary in python with a different rate coupon for each day of the week.

discount_code={}
for i in range(1,8):
    print("Enter coupon code for day" , i)
    code=input()
    discount_code[i]=code

print("Discount coupon code for each day as ") 
for x,y in discount_code.items():
    print(x,y)   