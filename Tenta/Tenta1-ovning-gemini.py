# 1a: Inte terminera

# 1b: snö
s = "snöboll"
n = len(s)
if s[0] == s[-1] or n < 6:
    print("vinter")
elif s[1:3] == "nö":
    print("kallt")
else:
    print("snö")

# 1c: []
lst = []
for i in range(1, 6, 2):
    lst.append(str(i) * i)
print(lst)

# 1d: 25.5
x = float(str(int("1" + "2") * 2) + ".5") + int(1.5)
print(x)

# 2:
def find_index(data, val):
    i = 0
    while i < len(data):
        if data[i] == val:
            return i
        i += 1
    return None

# 3a: 
lst0 = [-1, 1, 0, 2]
lstA0 = [1, 2]

# 3b: 
lst1 = [-1, 1, 0, 2]
lstA1 = [1, 0, 2]
# Är lst1 och lstA1 alias? Ja