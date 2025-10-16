# En liten klass som håller ett telefonnummer.
# Om flera namn pekar på samma Entry-objekt fungerar de som alias.
class Entry:
    def __init__(self, name):
        self.names = {name}  # håller alla namn (alias) för detta nummer


# Klassen som sköter själva telefonboken
class PhoneBook:
    def __init__(self):
        # Flera namn kan peka på samma Entry
        self.numbers = {}  # number -> Entry

    # Hjälpfunktion: kolla om ett nummer redan används av någon annan
    def number_in_use(self, my_entry, number):
        # Returnerar True om telefonnumret redan används av någon annan
        entry = self.numbers.get(number)
        return entry is not None and entry is not my_entry

    # Kommandon

    def add(self, name, number):
        # Lägg till nytt namn. Fel om namnet finns eller numret redan används.
        # kolla om namnet redan finns på något nummer
        for e in self.numbers.values():
            if name in e.names:
                print(f"{name} already exists")
                return
        if number in self.numbers:
            print(f"{number} already exists")
            return
        self.numbers[number] = Entry(name)

    def lookup(self, name):
        # hitta numret (key) där detta namn finns
        for number, entry in self.numbers.items():
            if name in entry.names:
                print(number)
                return
        print(f"{name} not found")

    def alias(self, name, newname):
        # Skapa alias. newname pekar på name
        # hitta entry för 'name'
        target_entry = None
        for entry in self.numbers.values():
            if name in entry.names:
                target_entry = entry
            if newname in entry.names:
                print("name not found or duplicate name")
                return
        if target_entry is None:
            print("name not found or duplicate name")
            return
        target_entry.names.add(newname)  # båda namnen pekar nu på samma Entry/nummer

    def change(self, name, number):
        # hitta entry + gammalt nummer (key) för 'name'
        old_number = None
        entry = None
        for num, e in self.numbers.items():
            if name in e.names:
                old_number, entry = num, e
                break
        if entry is None:
            print(f"{name} not found")
            return
        if self.number_in_use(entry, number):
            print(f"{number} already exists")
            return
        # flytta entry till nytt nummer (key)
        del self.numbers[old_number]
        self.numbers[number] = entry  # ändra numret, alias följer automatiskt

    def save(self, filename):
        # Spara alla namn och alias som separata rader
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for number, entry in self.numbers.items():
                    for name in entry.names:
                        file.write(f"{number};{name};\n")
        except OSError as err:
            print(f"could not save: {err}")

    def load(self, filename):
        # Load, Ersätt telefonboken. Varje rad blir en separat Entry
        try:
            with open(filename, "r") as file:
                self.numbers.clear()
                line_no = 0
                for line in file:
                    line_no += 1
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) < 2 or not parts[0] or not parts[1]: # Kollar trasiga rader
                        print(f"bad line {line_no}: {line}")
                        continue
                    number, name = parts[0], parts[1]
                    # skapa eller uppdatera entry för detta nummer
                    entry = self.numbers.get(number)
                    if entry is None:
                        entry = Entry(name)
                        self.numbers[number] = entry
                    else:
                        entry.names.add(name)

        except FileNotFoundError:
            print("file not found")
        except OSError as err:
            print(f"could not load: {err}")

    # Denna funktion tar en textinmatning kör de olika kommandorna
    def handle_command(self, line):
        line = line.strip()
        if not line:
            return True # gör inget om raden är tom

        parts = line.split() # dela upp texten på mellanslag
        command = parts[0].lower() # kommandon är inte skiftlägeskänsliga
        args = parts[1:] # resten är argument

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



def repl(prompt = "phoneBook> "):
    book = PhoneBook()
    while True:
        try:
            print(prompt, end="")
            line = input()  # läs en rad från användaren
        except EOFError:
            break
        if not book.handle_command(line):
            break


def main():
    repl()


if __name__ == "__main__":
    main()
