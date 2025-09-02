# 1 Lista på ingredienser för antal personer
def recept(antal):
    print("smör:", (15/4)*antal)
    print("ströbröd:", (3/4)*antal)
    print("ägg:", (int((3/4)*antal)))
    print("strösocker:", (3/4)*antal)
    print("vaniljsocker:", (2/4)*antal)
    print("bakpulver:", (2/4)*antal)
    print("vetemjöl:", (3/4)*antal)
    print("smör:", (75/4)*antal)
    print("vatten:", (1/4)*antal)

# 2.1 Tid att blanda ingredienserna är 10 minuter plus 1 minuter per person
def tidblanda(antal):
    tid = 10 + (1 * antal)
    print("\n")
    print("Total tid att baka kakan är", tid, "minuter")

# 2.2 Tid att grädda kakan är 40 minuter plus 2 minuter per person
def tidgradda(antal):
    tid = 40 + (2 * antal)
    print("\n")
    print("Total tid att grädda kakan är", tid, "minuter")

# 3 Sammanlagd tid att baka kakan
def sockerkaka(antal):
    print("\n\n\n")
    print("Det är", antal, "personer som ska äta sockerkakan.\n")
    recept(antal)
    tidblanda(antal)
    tidgradda(antal)
    print("Totalt tar det", (10 + 1 * antal) + (40 + 2 * antal), "minuter att baka sockerkakan för", antal, "personer.")

# Huvudprogram (script) som skriver ut recept för 4 och 7 personer
sockerkaka(4)
sockerkaka(7)