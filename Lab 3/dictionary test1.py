def insert(dictionary):
    word = input("Skriv vilket ord: ")
    description = input("Beskrivning av ordet: ")
    dictionary[word] = description
    print(f"'{word}' sparades i ordboken")


#def lookup(dictionary):


def menu():
    
    dictionary = []
    
    while True:
        
        print("\n1: Insert\n2: Lookup\n3: Exit\n")
    
        choose = int(input("Choose a number: "))

        if choose == 1:
            insert(dictionary)

        #elif choose == 2:
        #    lookup(dictionary)

        elif choose == 3:
            return
        
        
menu()