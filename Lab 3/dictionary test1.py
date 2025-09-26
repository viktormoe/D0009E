def insert(dictionary):
    word = input("Skriv vilket ord: ")
    if word in dictionary:
        print(f"Ordet {word} finns redan")
    else:
        description = input("Beskrivning av ordet: ")
        dictionary[word] = description
        print(f"\n'{word}' sparades i ordboken med beskrivningen '{description}'")


def lookup(dictionary):
    word = input("Vilket ord vill du kolla upp: ")
    print(f"\nOrdet '{word}' har beskrivningen: {dictionary[word]}")


def delete(dictionary):
    word = input("Vilket ord vill du radera: ")
    del dictionary[word]
    print(f"\nOrdet '{word}' har raderats")



def menu():
    dictionary = {}
    while True:
        print("\n----Meny----\n1: Insert\n2: Lookup\n2.5: Radera\n3: Exit\n")
        choose = input("Choose a number: ")

        if choose == "1":
            insert(dictionary)

        elif choose == "2":
            lookup(dictionary)

        elif choose == "2.5":
            delete(dictionary)

        elif choose == "3":
            print("Hejdå")
            return False

        else:
            print("Fel, försök igen med en valbar siffra")
        

        
menu()