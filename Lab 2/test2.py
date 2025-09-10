
print("\nRekursiv:")

def bounce(n):
    if  (n > 0):
        print(n)
        bounce(n - 1)
    print(n)

bounce(5)

print("\n\nIterativ:")

def bounce2(n):
    for i in range(n,0,-1):
        print(i)

    for i in range(0,n+1,1):
        print(i) 

bounce2(5)

print("\n")

bounce(0)

print("\n")

bounce2(0)


print("\n\nIterativ:")

def bounce3(n):
    i = n
    while i > 0:   # same as for i in range(n,0,-1)
        print(i)
        i -= 1

    i = 0
    while i <= n:  # same as for i in range(0,n+1,1)
        print(i)
        i += 1

bounce3(6)
