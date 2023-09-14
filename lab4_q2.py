x=int(input("enter the first number"))
y=int(input("enter the second nuber"))
n=int(input("enter the third number"))

i=x+1
while x<i and i<=y:
    if i%n==0:
        print(i)

    i=i+1
