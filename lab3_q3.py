a=float(input(" first side of the triagle"))
b=float(input("second side of the triangle"))
c=float(input("third side of the triangle"))
if a<b+c or b<c+a or c<a+b:
    print("they form side of a triangle")
else:
    print("they does not form side of a triangle")      

