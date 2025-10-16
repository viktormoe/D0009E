
# En liten klass som håller ett telefonnummer.
# Om flera namn pekar på samma Entry-objekt fungerar de som alias.
class Entry:
    def __init__(self, number):
        self.number = number


# Klassen som sköter själva telefonboken
class PhoneBook:
    def __init__(self):
        # Flera namn kan peka på samma Entry = alias.
        self.names = {}

    # Hjälpfunktion: kolla om ett nummer redan används av någon annan Entry
    def number_in_use(self, my_entry, number):
        # Returnerar True om telefonnumret redan används av någon annan Entry.
        for entry in self.names.values():
            if entry is not my_entry and entry.number == number:
                return True
        return False

    # Kommandon

    def add(self, name, number):
        # Lägg till nytt namn. Fel om namnet finns eller numret redan används.
        if name in self.names:
            print(f"{name} already exists")
            return
        if self.number_in_use(None, number):
            print(f"{number} already exists")
            return
        self.names[name] = Entry(number)

    def lookup(self, name):
        entry = self.names.get(name)
        if entry is None:
            print(f"{name} not found")
        else:
            print(entry.number)

    def alias(self, name, newname):
        # Skapa alias. newname pekar på name
        entry = self.names.get(name)
        if entry is None or newname in self.names:
            print("name not found or duplicate name")
            return
        self.names[newname] = entry  # båda namnen pekar nu på samma Entry/nummer

    def change(self, name, number):
        entry = self.names.get(name)
        if entry is None:
            print(f"{name} not found")
            return
        if self.number_in_use(entry, number):
            print(f"{number} already exists")
            return
        entry.number = number  # ändra numret, alias följer automatiskt

    def save(self, filename):
        # Spara alla namn och alias som separata rader
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for name, entry in self.names.items():
                    file.write(f"{entry.number};{name};\n")
        except OSError as err:
            print(f"could not save: {err}")

    def load(self, filename):
        # Load, Ersätt telefonboken. Varje rad blir en separat Entry
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.names.clear()
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
                    self.names[name] = Entry(number)
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
            print(prompt, end="", flush=True)
            line = input()  # läs en rad från användaren
        except EOFError:
            break  # avsluta om användaren trycker Ctrl-D

        # Hantera kommandot. False betyder att användaren skrev "quit".
        if not book.handle_command(line):
            break


def main():
    # All körning sker via funktioner
    repl("phoneBook> ")


if __name__ == "__main__":
    main()
