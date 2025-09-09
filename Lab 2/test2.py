
print("Rekursiv")

def bounce(n):
    if  (n > 0):
        print(n)
        bounce(n - 1)
    print(n)


bounce(5)