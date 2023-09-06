b=int(input())
hra=0.2*b
t=0.05*b
da=0.1*b
l=100000
g=hra+t+da
print("gross salary is ",g)

if g <3*l:
    print("0%")
elif g*l>=3*l and g*l<10*l:
    print("10%")
elif g*l>=10*l and g*l<25*l:
    print("20%")
else:
    print("30%")