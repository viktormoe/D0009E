def writeToFile(filnamn, sLst):
    f=open(filnamn,"w")
    for e in sLst:
        try:
            e != ""
        except ValueError:
            print("Tom sträng!")
        f.write(e+"\n")
    f.close()

def inputList(): # behöver ej skrivas av eller modifieras
    sLst=[]
    while True:
        s=input("Skriv in: ")
        if s=="exit":
            break
        sLst.append(s)
    return sLst

def inputfil():
    while True:
        filnamn = input("Skriv in filnamn: ")
        try:
            f = open(filnamn, "x")   # "x" = skapa ny fil, fel om den redan finns
            f.close()
            return filnamn           # om det lyckas, avsluta funktionen
        except FileExistsError:
            print("Filen finns redan, försök igen!")



def writeUI():
    filnamn = inputfil()
    sLst = inputList()
    writeToFile(filnamn, sLst)


writeUI()