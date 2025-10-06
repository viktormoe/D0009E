class Board:
    def __init__(self, msg):
        self.message = msg

def main():
    board1 = Board("")
    board2 = Board("")

    kim = board1
    chris = board2

    while True:
        print("\n=== Bulletin board system ===")
        print("Kim reads message:", kim.message)
        print("Chris reads message:", chris.message)
        print("\n1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            if kim == board1:
                kim = board2
                print("Kim is now at board 2")
            else:
                kim = board1
                print("Kim is now at board 1")
        elif choice == "2":
            if chris == board1:
                chris = board2
                print("Chris is now at board 2")
            else:
                chris = board1
                print("Chris is now at board 1")
        elif choice == "3":
            msg = input("Enter message for Kim to post: ")
            kim.message += " " + msg
            print("Kim posted a message on current board.")
        elif choice == "4":
            msg = input("Enter message for Chris to post: ")
            chris.message += " " + msg
            print("Chris posted a message on current board.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()