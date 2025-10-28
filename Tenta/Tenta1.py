def writeIntList(intLst, filename):
    try:
        with open(filename,"x") as f:
            for e in intLst:
                f.write(str(e)+"\n")
    except FileExistsError:
        raise FileException
   

# get int list from user
# do not modify
def inputInt():
    lst=[]
    while True:
        s=input("Number:")
        if s=="":
            return lst
        lst.append(int(s))


def intUI():
    user_filename = input("Filename: ")
    lst=inputInt()

    try:
        writeIntList(lst, user_filename)
    
    except FileException:
        print("File already exists")
