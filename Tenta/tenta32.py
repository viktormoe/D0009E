"""
Skriv en rekursiv funktion, unique, som tar en lista, lst, som argument och returnerar 
en ny lista med endast unika element från lst (alla element ska endast finnas en gång i den 
nya listan även om samma element förekommer flera gånger i lst).
Inbyggda funktioner eller metoder för strängar, listor eller tupler får inte användas. Det är 
tillåtet att använda funktionerna len och range samt operatorn in.
Exempel:
>>> unique([1,2,1,3,9,2,7,6,8,3])
[1, 9, 2, 7, 6, 8, 3]

"""



def unique(lst):
    if len(lst) == 0:
        return []
    rest = unique(lst[1:])
    if lst[0] in rest:
        return rest
    else:
        return [lst[0]] + rest



print(unique([1,2,1,3,9,2,7,6,8,3]))
