def kostnad(P, r, a):
    k = P + (a + 1) * P * r / 2
    print("Den totala kostnaden efter", a, "år är", int(k), "kr.")

P = float(input("Ange lånebelopp: "))
r = float(input("Ange ränta (t.ex. 0.03 för 3%): "))
a = int(input("Ange antal år: "))

kostnad(P, r, a)
