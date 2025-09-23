
def insert_word(words, descriptions):
    word = input("Enter the word to insert: ")
    description = input("Enter the description: ")
    if word in words:
        print(f"The word '{word}' already exists.")
    else:
        words.append(word)
        descriptions.append(description)
        print(f"Word '{word}' inserted successfully.")


def lookup_word(words, descriptions):
    word = input("Enter the word to lookup: ")
    if word in words:
        index = words.index(word)
        print(f"Description for '{word}': {descriptions[index]}")
    else:
        print(f"The word '{word}' does not exist.")


def show_all_words(words, descriptions):
    if words:
        print("All words in the dictionary:")
        for i in range(len(words)):
            print(f"{words[i]}: {descriptions[i]}")
    else:
        print("The dictionary is empty.")


def delete_word(words, descriptions):
    word = input("Enter the word to delete: ")
    if word in words:
        index = words.index(word)
        del words[index]
        del descriptions[index]
        print(f"Word '{word}' deleted successfully.")
    else:
        print(f"The word '{word}' does not exist.")


def menu():
    words = []
    descriptions = []
    while True:
        print("\nMenu for dictionary (two lists):")
        print("1. Insert")
        print("2. Lookup")
        print("3. Show all words")
        print("4. Delete")
        print("0. Exit")    
        choice = input("Choose an option: ")
        print("\n")

        if choice == "1":
            insert_word(words, descriptions)
        elif choice == "2":
            lookup_word(words, descriptions)
        elif choice == "3":
            show_all_words(words, descriptions)
        elif choice == "4":
            delete_word(words, descriptions)
        elif choice == "0":
            print("Goodbye!")
            return
        else:
            print("Invalid choice, try again.")

menu()