a=float(input("the three digit number"))
b=a//100
c=(a-(b*100))//10
d=a-(b*100+c*10)
sum=b+c+d
print("the sum of the digit",sum)
if sum%3==0:
    print("it is divisible by three")
else:
    print("it is not divisible by three")    
    