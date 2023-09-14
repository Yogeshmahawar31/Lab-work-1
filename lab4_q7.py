N = int(input("Enter the number of Fibonacci terms to generate: "))
a, b = 1, 1
count = 0
if N <= 0:
    print("Please enter a positive integer for N.")

while count < N:
        if count == 0:
            print(a, end=" ")  # Print the first term
        elif count == 1:
             print(b, end=" ")
        else:
            fib = a + b
            print(fib, end=" ")
            a, b = b, fib  
        count += 1
