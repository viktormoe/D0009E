
from typing import Optional

# En liten klass som håller ett telefonnummer.
# Om flera namn pekar på samma Entry-objekt fungerar de som alias.
class Entry:
    def __init__(self, number: str):
        self.number = number  # telefonnummer lagras som text (sträng)


# Klassen som sköter själva telefonboken (datastrukturen och kommandona)
class PhoneBook:
    def __init__(self):
        # Dictionary där varje namn pekar på en Entry (som innehåller numret)
        # Flera namn kan peka på samma Entry → alias.
        self.names: dict[str, Entry] = {}

    # Hjälpfunktion: kolla om ett nummer redan används av någon annan Entry
    def number_in_use(self, my_entry: Optional[Entry], number: str) -> bool:
        
        # Returnerar True om telefonnumret redan används av någon annan Entry.
        # my_entry används för att hoppa över aktuell post vid t.ex. 'change'.
        
        for entry in self.names.values():
            if entry is not my_entry and entry.number == number:
                return True
        return False

    # Kommandon

    def add(self, name: str, number: str) -> None:
        # Lägg till nytt namn. Fel om namnet finns eller numret redan används.
        if name in self.names:
            print(f"{name} already exists")
            return
        if self.number_in_use(None, number):
            print(f"{number} already exists")
            return
        self.names[name] = Entry(number)

    def lookup(self, name: str) -> None:
        entry = self.names.get(name)
        if entry is None:
            print(f"{name} not found")
        else:
            print(entry.number)

    def alias(self, name: str, newname: str) -> None:
        # Skapa alias: låt `newname` peka på samma Entry som `name`.
        entry = self.names.get(name)
        if entry is None or newname in self.names:
            print("name not found or duplicate name")
            return
        self.names[newname] = entry  # båda namnen pekar nu på samma Entry/nummer

    def change(self, name: str, number: str) -> None:
        entry = self.names.get(name)
        if entry is None:
            print(f"{name} not found")
            return
        if self.number_in_use(entry, number):
            print(f"{number} already exists")
            return
        entry.number = number  # ändra numret, alias följer automatiskt

    def save(self, filename: str) -> None:
        # Spara alla namn (även alias) som separata rader: "nummer;namn;".
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for name, entry in self.names.items():
                    file.write(f"{entry.number};{name};")
        except OSError as err:
            print(f"could not save: {err}")

    def load(self, filename: str) -> None:
        # Läs fil och ersätt telefonboken. Varje rad blir en separat Entry (alias försvinner).
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.names.clear()
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) < 2 or not parts[0] or not parts[1]:
                        # Hoppa över trasiga rader tyst (kan ändras till felmeddelande vid behov)
                        continue
                    number, name = parts[0], parts[1]
                    self.names[name] = Entry(number)
        except FileNotFoundError:
            print("file not found")
        except OSError as err:
            print(f"could not load: {err}")

    # Denna funktion tar en textinmatning och avgör vilket kommando som ska köras
    def handle_command(self, line: str) -> bool:
        line = line.strip()
        if not line:
            return True  # gör inget om raden är tom

        parts = line.split()               # dela upp texten på mellanslag
        command = parts[0].lower()         # kommandon är inte skiftlägeskänsliga
        args = parts[1:]                   # resten är argument

        # Välj och kör rätt kommando + skriv ut tydliga usage-texter vid fel antal argument
        if command == "add":
            if len(args) == 2:
                self.add(args[0], args[1])
            else:
                print("usage: add name number")
        elif command == "lookup":
            if len(args) == 1:
                self.lookup(args[0])
            else:
                print("usage: lookup name")
        elif command == "alias":
            if len(args) == 2:
                self.alias(args[0], args[1])
            else:
                print("usage: alias name newname")
        elif command == "change":
            if len(args) == 2:
                self.change(args[0], args[1])
            else:
                print("usage: change name number")
        elif command == "save":
            if len(args) == 1:
                self.save(args[0])
            else:
                print("usage: save filename")
        elif command == "load":
            if len(args) == 1:
                self.load(args[0])
            else:
                print("usage: load filename")
        elif command == "quit":
            return False  # avsluta programmet
        else:
            print("unknown command")
        return True  # fortsätt köra


# Programloopen – körs tills användaren skriver "quit"

def repl(prompt: str = "phoneBook> "):
    book = PhoneBook()
    while True:
        try:
            print(prompt, end="", flush=True)
            line = input()  # läs en rad från användaren
        except EOFError:
            break  # avsluta om användaren trycker Ctrl-D

        # Hantera kommandot. False betyder att användaren skrev "quit".
        if not book.handle_command(line):
            break


def main():
    repl("phoneBook> ")


if __name__ == "__main__":
    main()
