#!/usr/bin/env python3
"""
Telefonbok – kort klassbaserad version med många kommentarer.
Mål: vara lätt att läsa och förstå, men ändå följa labbkraven.

Kommandon (en rad, separerade med valfritt antal whitespace):
  add name number      – lägg till nytt namn (namn och nummer måste vara unika)
  lookup name          – skriv ut numret för ett namn (eller alias)
  alias name newname   – gör nytt namn som pekar på *samma* nummer som `name`
  change name number   – byt nummer för ett namn/alias (påverkar alla alias)
  save filename        – spara "nummer;namn;" per rad (alias sparas som vanliga namn)
  load filename        – läs fil, ersätt hela telefonboken (aliasrelationer försvinner)
  quit                 – avsluta programmet
"""

PROMPT = "phoneBook> "  # texten som visas innan input – fritt enligt uppgiften

# --- Liten klass som håller numret ---
class Entry:
    """En post i telefonboken. Håller bara ett telefonnummer.
    Den är medvetet *muterbar* (fältet kan ändras), så att alias fungerar enkelt:
    Flera namn kan peka på samma Entry-objekt. Om numret ändras på Entry:n så ser
    alla namn som pekar hit den nya siffran direkt.
    """
    def __init__(self, n: str):
        self.n = n  # telefonnummer som sträng


# --- Själva telefonboken ---
class PhoneBook:
    def __init__(self):
        # `names` mappar *varje* namn (inklusive alias) till en Entry.
        # Två olika namn kan alltså peka på samma Entry-objekt → det är alias.
        self.names: dict[str, Entry] = {}

    # Hjälpmetod: kolla om ett nummer redan används av någon ANNAN post
    def _num_used(self, me: Entry | None, num: str) -> bool:
        for e in self.names.values():
            # hoppa över "mig själv" när vi ändrar (so we can keep same number)
            if e is not me and e.n == num:
                return True
        return False

    # --- Kommandon ---
    def add(self, name: str, num: str) -> None:
        """Lägg till nytt namn med nummer.
        Fel om namnet finns redan eller om numret redan används.
        """
        if name in self.names:
            print(f"{name} already exists"); return
        if self._num_used(None, num):
            print(f"{num} already exists"); return
        self.names[name] = Entry(num)  # nytt Entry, inget alias ännu

    def lookup(self, name: str) -> None:
        """Skriv ut numret för `name` eller fel om det inte finns."""
        e = self.names.get(name)
        print(e.n if e else f"{name} not found")

    def alias(self, name: str, newname: str) -> None:
        """Skapa alias: låt `newname` peka på samma Entry som `name`.
        `name` måste finnas och `newname` får inte finnas.
        """
        e = self.names.get(name)
        if e is None or newname in self.names:
            print("name not found or duplicate name"); return
        self.names[newname] = e  # pekar på samma Entry → delar nummer

    def change(self, name: str, num: str) -> None:
        """Ändra numret för ett befintligt namn/alias.
        Påverkar alla alias, eftersom de delar samma Entry.
        """
        e = self.names.get(name)
        if e is None:
            print(f"{name} not found"); return
        if self._num_used(e, num):
            print(f"{num} already exists"); return
        e.n = num  # byt själva siffervärdet i Entry-objektet

    def save(self, filename: str) -> None:
        """Spara en rad per namn i formatet "nummer;namn;".
        Alias behandlas som vanliga namn (det är tillåtet enligt uppgiften).
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for k, e in self.names.items():
                    f.write(f"{e.n};{k};")
        except OSError as err:
            print(f"could not save: {err}")

    def load(self, filename: str) -> None:
        """Läs in fil och ersätt hela telefonboken.
        Varje rad skapar ett *eget* Entry – aliasrelationer återskapas inte.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.names.clear()  # kasta allt i minnet först
                for line in f:
                    line = line.strip()
                    if not line: 
                        continue
                    parts = line.split(";")  # förväntar oss: nummer;namn;
                    if len(parts) < 2 or not parts[0] or not parts[1]:
                        # hoppa över trasiga rader tyst
                        continue
                    num, name = parts[0], parts[1]
                    self.names[name] = Entry(num)  # nytt separat Entry → inget alias
        except FileNotFoundError:
            print("file not found")
        except OSError as err:
            print(f"could not load: {err}")

    # --- Enkel parser/dispatcher ---
    def handle(self, line: str) -> bool:
        """Ta emot en textrad, kör rätt kommando, returnera False om vi ska avsluta.
        Vi delar upp på whitespace, gör kommandon case-insensitive och skriver
        begripliga fel vid fel antal argument.
        """
        line = line.strip()
        if not line:
            return True  # tom rad gör ingenting

        p = line.split()
        cmd, args = p[0].lower(), p[1:]

        if   cmd == "add":
            (len(args)==2 and self.add(*args))    or print("usage: add name number")
        elif cmd == "lookup":
            (len(args)==1 and self.lookup(*args)) or print("usage: lookup name")
        elif cmd == "alias":
            (len(args)==2 and self.alias(*args))  or print("usage: alias name newname")
        elif cmd == "change":
            (len(args)==2 and self.change(*args)) or print("usage: change name number")
        elif cmd == "save":
            (len(args)==1 and self.save(*args))   or print("usage: save filename")
        elif cmd == "load":
            (len(args)==1 and self.load(*args))   or print("usage: load filename")
        elif cmd == "quit":
            return False
        else:
            print("unknown command")
        return True

# --- REPL (Read–Eval–Print Loop) ---
# En liten loop som skriver prompt, läser en rad, kör kommandot och upprepar.

def repl() -> None:
    pb = PhoneBook()
    while True:
        try:
            print(PROMPT, end="", flush=True)
            line = input()
        except EOFError:
            break  # t.ex. Ctrl-D
        if not pb.handle(line):
            break

if __name__ == "__main__":
    repl()
