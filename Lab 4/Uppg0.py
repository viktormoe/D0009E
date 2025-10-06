# Vi skapar en klass som representerar en anslagstavla (Board)
class Board:
    # __init__ är en speciell funktion som körs när vi skapar ett nytt objekt av klassen
    # self betyder "denna instans" (denna specifika tavla)
    # msg är texten (meddelandet) som vi vill sätta på tavlan när den skapas
    def __init__(self, msg):
        # Vi sparar meddelandet i en variabel som tillhör just denna tavla
        self.message = msg


# Här skapar vi huvudfunktionen där själva programmet körs
def main():
    # Skapa två anslagstavlor (objekt av klassen Board)
    # De får varsin starttext
    board1 = Board("")
    board2 = Board("")

    # Skapa två personer: Kim och Chris
    # De "pekar" på (står framför) varsin tavla i början
    kim = board1
    chris = board2

    # while True betyder att loopen körs om och om igen tills vi bryter med 'break'
    while True:
        # Visa aktuell status: vad Kim och Chris ser just nu
        print("\n=== Bulletin board system ===")
        print("Kim reads message:", kim.message)
        print("Chris reads message:", chris.message)

        # Visa menyval
        print("\n1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: Exit")

        # Läs in användarens val (som en sträng)
        choice = input("Enter choice: ")

        # === MENYVAL ===

        # 1: Flytta Kim till den andra tavlan
        if choice == "1":
            # Om Kim står vid board1, flytta till board2, annars tvärtom
            if kim == board1:
                kim = board2
                print("Kim is now at board 2")
            else:
                kim = board1
                print("Kim is now at board 1")

        # 2: Flytta Chris till den andra tavlan
        elif choice == "2":
            if chris == board1:
                chris = board2
                print("Chris is now at board 2")
            else:
                chris = board1
                print("Chris is now at board 1")

        # 3: Kim lägger till ett meddelande på den tavla hen står vid
        elif choice == "3":
            # Fråga användaren vad Kim ska skriva
            msg = input("Enter message for Kim to post: ")
            # Lägg till det nya meddelandet på den aktuella tavlans text
            # Vi använder += för att lägga till på slutet (konkatenera)
            kim.message += " " + msg
            print("Kim posted a message on current board.")

        # 4: Chris lägger till ett meddelande på den tavla hen står vid
        elif choice == "4":
            msg = input("Enter message for Chris to post: ")
            chris.message += " " + msg
            print("Chris posted a message on current board.")

        # 0: Avsluta programmet
        elif choice == "0":
            print("Goodbye!")
            break  # Avbryt loopen -> programmet avslutas

        # Om man skriver något annat än 0-4
        else:
            print("Invalid choice, try again.")


# Detta ser till att main() körs om man startar filen direkt
# __name__ == "__main__" betyder att koden bara körs när man startar denna fil (inte när man importerar den)
if __name__ == "__main__":
    main()
