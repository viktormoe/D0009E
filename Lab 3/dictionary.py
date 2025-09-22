
def insert_word(dictionary):
    word = input("Enter the word to insert: ")
    description = input("Enter the description: ")
    if word in dictionary:
        print(f"The word '{word}' already exists in the dictionary.")
    else:
        dictionary[word] = description
        print(f"Word '{word}' inserted successfully.")


def lookup_word(dictionary):
    word = input("Enter the word to lookup: ")
    if word in dictionary:
        print(f"Description for '{word}': {dictionary[word]}")
    else:
        print(f"The word '{word}' does not exist in the dictionary.")


def show_all_words(dictionary):
    if dictionary:
        print("All words in the dictionary:")
        for word, description in dictionary.items():
            print(f"{word}: {description}")
    else:
        print("The dictionary is empty.")


def delete_word(dictionary):
    word = input("Enter the word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"Word '{word}' deleted successfully.")
    else:
        print(f"The word '{word}' does not exist in the dictionary.")


def menu_disc():
    dictionary = {}
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
            insert_word(dictionary)
            continue

        elif choice == "2":
            lookup_word(dictionary)
            continue

        elif choice == "3":
            show_all_words(dictionary)
            continue

        elif choice == "4":
            delete_word(dictionary)
            continue

        elif choice == "0":
            print("Goodbye!")
            return False
        else:
            print("Invalid choice, try again.")
        return True
                    

menu_disc()
