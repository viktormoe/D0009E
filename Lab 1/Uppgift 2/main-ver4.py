
# 1 Lista på ingredienser för antal personer
def recept(antal):
    print("smör:", (15/4)*antal, "g")
    print("ströbröd:", (3/4)*antal, "msk")
    print("ägg:", (int((3/4)*antal)), "st")
    print("strösocker:", (3/4)*antal, "dl")
    print("vaniljsocker:", (2/4)*antal, "tsk")
    print("bakpulver:", (2/4)*antal, "tsk")
    print("vetemjöl:", (3/4)*antal, "dl")
    print("smör:", (75/4)*antal, "g")
    print("vatten:", (1/4)*antal, "dl")


# 2.1 Tid att blanda ingredienserna är 10 minuter plus 1 minuter per person
def tidblanda(antal):
    tid1 = 10 + (1 * antal)
    return tid1


# 2.2 Tid att grädda kakan är 40 minuter plus 2 minuter per person
def tidgradda(antal):
    tid2 = 30 + (3 * antal)
    return tid2


# 3 Sammanlagd tid att baka kakan
def sockerkaka(antal):
    print("\n")
    print("Det är", antal, "personer som ska äta sockerkakan.\n")
    recept(antal)
    print("\nTotalt tar det", tidblanda(antal) + tidgradda(antal), "minuter att baka sockerkakan för", antal, "personer.")


# Huvudprogram (script) som skriver ut recept för 4 och 7 personer
print("-"*45)

sockerkaka(4)

print("-"*45)

sockerkaka(7)