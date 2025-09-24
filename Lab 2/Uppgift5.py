
import math


print("\n5a:")

# 5a   
def derivata(f, x, h):
    approx = (f(x + h) - f(x - h)) / (2 * h)        
                                                 
    return approx


# Kör derivatafunktionen med f = sin, x = pi, och steglängden h = 0.001
print("sin test:", derivata(math.sin, math.pi, 0.001), "=", math.cos(math.pi))


print("\n5b:")


# 5b
def solve(f, x0, h):
    x = x0
    while True:
        d = derivata(f, x, h)      
        if d == 0:                   
            return None
        x_new = x - f(x) / d         
        if abs(x_new - x) < h:       
            return x_new
        x = x_new

# Test
def f1(x): 
    return x**2 - 1
def f2(x): 
    return 2*x - 1
def f3(x): 
    return math.cos(x) - x

print("solve x^2-1=0, start=2:", solve(f1, 2, 1e-6))
print("solve 2x-1=0, start=0:", solve(f2, 0, 1e-6))
print("solve cos(x)-x=0, start=1:", solve(f3, 1, 1e-6))



