# I denna laboration ska vi implementera en enkel ordlista m.h.a. python. Ordlistan ska vara interaktiv och användaren ska kunna lägga till och slå upp ord i ordlistan. Själva ordlistan ska implementeras på tre olika sätt, med tre olika sätt att spara ordlistan. Följande tre olika sätt att lagra en ska ordlista implementeras:

# Två stycken listor av strängar. Den första listan innehåller ordet vi vill slå upp, och den andra listan innehåller beskrivningen för det ordet, på motsvarande position.
# En lista av tupler. En enda lista som består av par, där första delen av varje par är ordet vi vill slå upp, och den andra är beskrivningen. Observera här alltså att datastrukturen ska vara  en lista, varje element i denna lista ska i sin tur vara ett par (en tupel med två element).
# Ett dictionary. Ett dictionary som innehåller ordet vi vill slå upp som "nyckel" och tillhörande beskrivning som "värde".
# För varje lösning ska två operationer finnas: en för att sätta in och en för att slå upp ord i listan. Varje operation (och varje uppdatering av datastrukturen) ska implementeras som en egen funktion för att ge programmet bra struktur. Återanvänd gärna kod mellan de tre lösningarna (t.ex. kan du ha samma funktion som skriver ut själva menyn).

# Separera de tre lösningarna genom att välja olika namn på funktionerna för respektive operation. Varje lösning ska dessutom ha en egen funktion som startar just den lösningen.

# Ordlistan ska presentera användaren med en meny där det finns följande alternativ: 1: Insert, 2: Lookup. Användaren ska kunna välja alternativ genom mata in siffran för motsvarande operation. Programmet ska sedan fråga användaren efter vilket ord operationen ska verka på och sedan, i fallet med insert fråga efter ordets beskrivning. Det ska inte vara tillåtet att sätta in samma ord två gånger i ordlistan. Om användaren försöker göra det ska ett felmeddelande skrivas ut. I fallet med lookup ska beskrivningen för ordet, som finns lagrad, skrivas ut på skärmen. Om ordet som slås upp inte existerar i ordlistan så ska ett felmeddelande skrivas ut.

# Exempel på körning:

# >>> main_dic()
# Menu for dictionary

#  1: Insert
#  2: Lookup
#  3: Exit program

# Choose alternative: 1
# Word to insert: dator
# Description of word: en manick som inte fungerar
# Menu for dictionary

#  1: Insert
#  2: Lookup
#  3: Exit program

# Choose alternative: 2
# Word to lookup: dator
# Description for dator : en manick som inte fungerar
# Menu for dictionary

#  1: Insert
#  2: Lookup
#  3: Exit program

# Choose alternative: 3
# >>> 
# Frivillig extrauppgift: Lägg till funktionen "delete" i menyerna och implementera den. Funktionen tar bort ord (och beskrivning) från ordlistan.

def menu_disc():
    while True:
        print("\nMenu for dictionary:")
        print("1. Insert")
        print("2. Lookup")
        print("3. Show all words")
        print("4. Delete")
        print("0. Exit")    
        choice = input("Choose an option: ")
        print("\n")
        
        if choice == "1":
            word = input("Enter the word to insert: ")
            description = input("Enter the description: ")
            if word in dictionary:
                print(f"The word '{word}' already exists in the dictionary.")
            else:
                dictionary[word] = description
                print(f"Word '{word}' inserted successfully.")

        elif choice == "2":
            word = input("Enter the word to lookup: ")
            if word in dictionary:
                print(f"Description for '{word}': {dictionary[word]}")
            else:
                print(f"The word '{word}' does not exist in the dictionary.")

        elif choice == "3":
            if dictionary:
                print("All words in the dictionary:")
                for word, description in dictionary.items():
                    print(f"{word}: {description}")
            else:
                print("The dictionary is empty.")

        elif choice == "4":
            word = input("Enter the word to delete: ")
            if word in dictionary:
                del dictionary[word]
                print(f"Word '{word}' deleted successfully.")
            else:
                print(f"The word '{word}' does not exist in the dictionary.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


dictionary = {}
menu_disc()
