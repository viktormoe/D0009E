
print("\n")

# 1 Rekursiv funktion
print("Deluppgift 1:\n")
def bounce(n):
    print(n)
    if n > 0:
        bounce(n - 1)
        print(n)

bounce(4)


print("\n"*2)

# 2 Iterativ funktion
print("Deluppgift 2:\n")
def bounce2(n):
    for i in range(n, -1, -1):
        print(i)
    for i in range(1, n + 1, 1):
        print(i)

bounce2(4)

print("\n"*2)

# Testkod för deluppgift 1 och 2
import d0009e_lab2_bounceTest

print("\n"*2)


# 3 Tvärsumma Rekursiv
print("Deluppgift 3:\n")
def tvarsumman(n):
    if n < 10:
        return n
    else:
        return n % 10 + tvarsumman(n // 10)

print(tvarsumman(12345))

print("\n"*2)


# 4 Tvärsumman iterativt
print("Deluppgift 4:\n")
def tvarsumman2(n):
    summa = 0
    while n > 0:
        summa += n % 10
        n //= 10
    return summa

print(tvarsumman2(12345))

print("\n"*2)
import d0009e_lab2_sumTest

print("\n"*2)





