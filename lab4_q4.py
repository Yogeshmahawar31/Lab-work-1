N = int(input("Enter a positive number N: "))
divisible_count = 0
not_divisible_count = 0
while True:
    num = int(input("Enter a number (-999 to exit): "))
    if num == -999:
        break
    if num % N == 0:
        divisible_count += 1
    else:
        not_divisible_count += 1
print("Numbers divisible by N:", divisible_count)
print("Numbers not divisible by N:", not_divisible_count)
