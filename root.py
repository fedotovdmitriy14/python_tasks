import math

def find_roots(a, b, c):
    x1 = int(((-b+math.sqrt(b*b-4*a*c))/(2*a)))
    x2 = int(((-b-math.sqrt(b*b-4*a*c))/(2*a)))
    return x1, x2

print(find_roots(2, 10, 8))

