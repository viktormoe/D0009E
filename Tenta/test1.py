""" 
[1, 7, 4, 2, -1, 5, 3, 2, 9]
a) funktion som returnerar ett medelvärde
b) funktion som returnerar ett medianvärde
c) funktion som returnerar största, minsta värde
d) funktion som storleksordnar listan
e) funktion som byter ordning på listan 

"""


all = [1, 7, 4, 2, -1, 5, 3, 2, 9]


print("\n")
print("a)")

def medel():
    calc = sum(all) / len(all)
    print(calc)

medel()


print("\n")
print("b)")

def median():
    all.sort()
    antal = len(all)
    if antal % 2 == 0:
        # Jämnt antal element
        mid1 = all[antal // 2 - 1]
        mid2 = all[antal // 2]
        median_value = (mid1 + mid2) / 2
    else:
        # Udda antal element
        median_value = all[antal // 2]
    print(median_value)

median()


print("\n")
print("c)")

def BigSmall():
    print(max(all))
    print(min(all))

BigSmall()


print("\n")
print("d)")

def sort():
    all.sort()
    print(all)

sort()


print("\n")
print("e)")

def randomize():
    all.reverse()
    print(all)

randomize()
