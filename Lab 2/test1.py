# 1 Rekursiv
def bounce(n):
    print(n)
    if n>0:
        bounce(n-1)
        print(n)

bounce(4)

print("\n"*2)


# 2 Iterativ
def bounce2(n):
    for i in range(n,-1,-1):
        print(i)
    for i in range(1,n+1):
        print(i)


bounce2(5)

print("\n"*2)


# 3 Rekursiv
def tvarsumma(n):
    print(n)
    if 


tvarsumma(123456789)