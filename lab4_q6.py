n=int(input("enter the positive number"))
P,X = 0,n
while n>0:
    v=n%10
    P=P*10+v
    n=n//10
    print(P)
if P==X:
    print("palindrome")
else:
    print("not palindrom")        