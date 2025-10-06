# Enkel telefonbok – utan klasser
# Kör: python3 telefonbok.py

def add(phonebook, name, number):
    # Lägg till nytt namn och nummer
    if name in phonebook:
        print(f"{name} already exists")
        return
    if number in phonebook.values():
        print(f"{number} already exists")
        return
    phonebook[name] = number


def lookup(phonebook, name):
    # Sök upp ett namn
    if name not in phonebook:
        print(f"{name} not found")
    else:
        print(phonebook[name])


def alias(phonebook, name, newname):
    # Gör ett nytt alias (extra namn för samma nummer)
    if name not in phonebook or newname in phonebook:
        print("name not found or duplicate name")
        return
    phonebook[newname] = phonebook[name]


def change(phonebook, name, new_number):
    # Ändra numret för ett namn (och alla alias som delar samma nummer)
    if name not in phonebook:
        print(f"{name} not found")
        return

    # Kolla om nya numret redan används
    if new_number in phonebook.values():
        print(f"{new_number} already exists")
        return

    old_number = phonebook[name]

    # Ändra alla namn som har samma gamla nummer
    for key in list(phonebook.keys()):
        if phonebook[key] == old_number:
            phonebook[key] = new_number


def save(phonebook, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for name, number in phonebook.items():
                f.write(f"{number};{name};\n")
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Could not save file: {e}")


def load(filename):
    phonebook = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                if len(parts) >= 2:
                    number, name = parts[0], parts[1]
                    phonebook[name] = number
        print(f"Loaded {filename}")
    except FileNotFoundError:
        print("File not found")
    return phonebook


def main():
    phonebook = {}
    while True:
        command = input("phoneBook> ").strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0].lower()

        if cmd == "add" and len(parts) == 3:
            add(phonebook, parts[1], parts[2])

        elif cmd == "lookup" and len(parts) == 2:
            lookup(phonebook, parts[1])

        elif cmd == "alias" and len(parts) == 3:
            alias(phonebook, parts[1], parts[2])

        elif cmd == "change" and len(parts) == 3:
            change(phonebook, parts[1], parts[2])

        elif cmd == "save" and len(parts) == 2:
            save(phonebook, parts[1])

        elif cmd == "load" and len(parts) == 2:
            phonebook = load(parts[1])

        elif cmd == "quit":
            print("Goodbye!")
            break

        else:
            print("Unknown or invalid command")


if __name__ == "__main__":
    main()
