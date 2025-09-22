# I denna laboration ska vi titta lite närmare på funktionsbegreppet och (i de två första deluppgifterna) begreppet
# rekursion och iteration (iteration betyder att man ska använda en loop ("snurra")).

# Skriv en funktion bounce(n) som givet ett naturligt tal (heltal >=0) n skriver ut alla tal från 0 till n på skärmen, först i
# fallande och sedan i stigande ordning. Exempel:

# >>> bounce(4)
# 4
# 3
# 2
# 1
# 0
# 1
# 2
# 3
# 4
# >>> bounce(0)
# 0

# Funktionen ska implementeras med hjälp av rekursion. Tips: ett komma i slutet på print-satsen undertrycker
# det radbyte som annars sker efter varje utskrift.
# Skriv en funktion bounce2(n)som utför samma sak som funktionen bounce(n), men inte är rekursiv utan iterativ. Iterativ betyder att den ska använda en loop (eller "snurra").
# Skriv en funktion, tvarsumman, som beräknar tvärsumman av ett naturligt tal (funktionen ska ta ett heltal som argument). Med tvärsumman menas summan av alla siffror i talet i talbasen 10 (alltså så som vi vanligtvis skriver talet). Problemet ska lösas med en rekursiv funktion. Här är det inte tillåtet att konvertera talet till en sträng först.
# Ledning: ett naturligt tal kan delas upp i en sista siffra och det tal man får om man "tar bort" den sista siffran
# (här är operatorerna % och / lämpliga att använda). Om det inte blir något kvar när sista siffran tagits bort är
# lösningen enkel, i annat fall har man fått ett nytt tal vars tvärsumma är en del av det sökta svaret.
# Skriv en funktion, tvarsumman2, som utför samma sak som funktionen i uppgift 3, men inte är rekursiv utan iterativ.

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





