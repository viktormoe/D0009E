def insert_word(dictionary):
    word = input("Enter the word to insert: ")
    description = input("Enter the description: ")
    if any(w == word for (w, d) in dictionary):
        print(f"The word '{word}' already exists.")
    else:
        dictionary.append((word, description))
        print(f"Word '{word}' inserted successfully.")


def lookup_word(dictionary):
    word = input("Enter the word to lookup: ")
    for w, d in dictionary:
        if w == word:
            print(f"Description for '{word}': {d}")
            return
    print(f"The word '{word}' does not exist.")


def delete_word(dictionary):
    word = input("Enter the word to delete: ")
    for i, (w, d) in enumerate(dictionary):
        if w == word:
            del dictionary[i]
            print(f"Word '{word}' deleted successfully.")
            return
    print(f"The word '{word}' does not exist.")


def menu():
    dictionary = []
    while True:
        print("\nMenu for dictionary (list of tuples):")
        print("1. Insert")
        print("2. Lookup")
        print("3. Delete")
        print("0. Exit")    
        choice = input("Choose an option: ")
        print("\n")

        if choice == "1":
            insert_word(dictionary)

        elif choice == "2":
            lookup_word(dictionary)

        elif choice == "3":
            delete_word(dictionary)

        elif choice == "0":
            print("Goodbye!")
            return
        
        else:
            print("Invalid choice, try again.")


menu()