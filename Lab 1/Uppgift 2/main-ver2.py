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

recept(4)


# 2.1 Tid att blanda ingredienserna är 10 minuter plus 1 minuter per person
def tidblanda(antal):
    tid = 10 + (1 * antal)
    print("\n")
    print("Total tid att baka kakan är", tid, "minuter")

tidblanda(4)


# 2.2 Tid att grädda kakan är 40 minuter plus 2 minuter per person
def tidgradda(antal):
    tid = 30 + (3 * antal)
    print("\n")
    print("Total tid att grädda kakan är", tid, "minuter")

tidgradda(4)


# 3 Sammanlagd tid att baka kakan
def sockerkaka(antal):
    print("\n\n\n")
    print("Det är", antal, "personer som ska äta sockerkakan.\n")
    recept(antal)
    tidblanda(antal)
    tidgradda(antal)
    print("Totalt tar det", (10 + 1 * antal) + (30 + 3 * antal), "minuter att baka sockerkakan för", antal, "personer.")

sockerkaka(4)


# 4 Skriver ut recept för 4 och 7 personer

