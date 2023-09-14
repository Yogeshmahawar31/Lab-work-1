N = int(input("Enter a positive integer N: "))
if N < 0:
    print("invalid number","please enter a positive number")
factorial = 1
if N == 0:
    factorial = 1
else:
    while N > 0:
        factorial *= N
        N -= 1
print("Factorial:", factorial)
