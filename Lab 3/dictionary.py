
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



def delete_word(dictionary):
    word = input("Enter the word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"Word '{word}' deleted successfully.")
    else:
        print(f"The word '{word}' does not exist in the dictionary.")


def menu():
    dictionary = {}
    while True:
        print("\nMenu for dictionary:")
        print("1. Insert")
        print("2. Lookup")
        print("3. Delete")
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
            delete_word(dictionary)
            continue

        elif choice == "0":
            print("Goodbye!")
            return False
        
        else:
            print("Invalid choice, try again.")
        return True
                    

menu()
