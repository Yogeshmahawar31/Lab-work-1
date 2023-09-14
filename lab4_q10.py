a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c:"))
d= b**2 - 4*a*c

if d > 0:
    # Two real and distinct solutions
    x1 = (-b + ((b**2)-4*a*c)) / (2*a)
    x2 = (-b -( (b**2)-4*a*c)) / (2*a)
    print(f"Solutions: {x1:.2f}, {x2:.2f}")
elif d == 0:
    
    x = -b / (2*a)
    print(f"Solution: {x:.2f}")
else:
    # No real solutions (complex)
    print("No real solutions.")
