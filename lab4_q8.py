num = int(input("Enter an integer: "))
if num <= 1:
    print("enter the positive number")

is_prime = True

i = 2
while i * i <= num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

# Display the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

