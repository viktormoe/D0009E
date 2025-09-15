
# 0a
print("0a:")

# Iteration
def EttTillFem():
    for tal in range(1,6,1):
        print(tal)

EttTillFem()

print("\n")


# Rekursion
def EttTillFem2(n=1):
    if n > 5:
        return
    print(n)
    EttTillFem2(n+1)

EttTillFem2()

print("\n"*2)


# 0b
print("0b:")

# Iteration
def FemTillEtt():
    for tal in range(5,0,-1):
        print(tal)

FemTillEtt()

print("\n")


# Rekursion
def FemTillEtt2(n):
    print(n)
    if n > 1:
        FemTillEtt2(n-1)
    
FemTillEtt2(5)

print("\n"*2)


# 1a
print("1a")

# Iteration
def NollTillN(n):
    for n in range(0, n+1, 1):
        print(n)

NollTillN(6)

print("\n")

#Rekursion
def NollTillN2(n):
    if n > 0:
        NollTillN2(n-1)
    print(n)

NollTillN2(5)



print("\nTest1")


def bounce5(n):
    if (n > 0):
        print(n)
        bounce5(n-1)
    if (n < )


bounce5(5)