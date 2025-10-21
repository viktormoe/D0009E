def readFloat():
    f=open("testfil","r")
    value = float(f.readline())
    f.close()
    return value

def readUI():
    value = readFloat()
    print(value)