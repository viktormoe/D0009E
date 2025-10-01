'''
Glöm inte att beakta kodstilen i denna lab. Denna laboration syftar till att öva användning av dictionaries och objekt (även om detta inte är ett krav), i synnerhet vad gäller hantering av alias. Dessutom kommer programmet som ska skrivas att vara interaktivt. Viss rudimentär felhantering kommer också att behövas, men om detta ska implementeras med hjälp av Python's exceptions är en designfråga där beslutet är ert eget.

Laborationsuppgiften är att skriva ett interaktivt program som hanterar en dynamisk telefonbok via en uppsättning enkla kommandon (dynamisk betyder att det går att ändra i telefonboken). Kommandona ska alla vara en rad långa och kunna updelas i ord med whitespace emellan (ett eller flera whitespace ska accepteras av programmet).  Telefonboken kan antingen användas till gamla hederliga fasta telefonerLinks to an external site. (en antik företeelse som existerade förra seklet) eller till att hantera mer moderna mobiltelefonerLinks to an external site. som har tvillingkort (där då fler telefoner får samma nummer). Prompten kan vara helt valfri (prompt=det som skrivs ut innan programmet väntar på inmatning från användaren). Följande kommandon ska hanteras (fler får läggas till efter behag):

add name number – lägger till name med nummret number till telefonboken. Här är det tillåtet att begränsa sig till att namn måste vara unika (två olika personer med olika nummer kan inte heta likadant). Alla telefonnummer måste vara unika; det är alltså inte tillåtet att lägga till flera namn med samma telefonnummer som inte är alias (alias har alltid, per konstruktion, samma telefonnummer).
lookup name – skriver ut numret som finns lagrat för name.
alias name newname – låter name bli sökbart även under namnet newname. Observera att name och newname blir helt likställda - newname fungerar i alla avseenden som name.
change name number – ändrar numret som associeras med det befintliga namnet name till number.
save filename – sparar innehållet i telefonboken till filen filename.
load filename – läser in innehållet från filen filename till telefonboken. Telefonboken i minnet kastas bort (efter inläsningen har vi endast telefonboken från filen i minnet).
quit – avslutar den interaktiva körningen
För kommandot add gäller att en felutskrift ska genereras om name redan finns definierat i telefonboken; för de övriga gäller att felutskrift ska ske om name inte är definierat. Med felutskrift menas att programet ska berätta vad som är fel på ett begripligt sätt och sedan skriva ut prompten igen. Namn som definierats som alias (med alias-kommandot) ska kunna användas i lookup-, change- och andra alias-kommandon på samma sätt som alla namn, så att följande beteende erhålls:

phoneBook> add Magdalena 123
phoneBook> add Maggan 123
123 already exists
phoneBook> add Magdalena 456
Magdalena already exists
phoneBook> add Karl 456
phoneBook> save testbok
phoneBook> alias test1 test2
name not found or duplicate name
phoneBook> alias Magdalena Karl
name not found or duplicate name
phoneBook> alias Magdalena Maggan
phoneBook> alias Maggan Magda
phoneBook> change test1 56
test1 not found
phoneBook> change Magda 456
456 already exists
phoneBook> change Maggan 789
phoneBook> lookup test1
test1 not found
phoneBook> lookup Magdalena
789
phoneBook> load testbok
phoneBook> lookup Magdalena
123
phoneBook> quit
>>>
Notera att programmet ska presentera en prompt ("telebok>" i det här fallet") och att användaren sedan ska kunna skriva ovanstående kommandon på beskrivet sätt. Det är inte tillåtet att ha en meny i denna uppgift.
Ett telefonnummer lagras lämpligtvis som en sträng. Ingen speciell kontroll av formatet på telefonnumret behöver göras (om användaren är dum nog att skriva in nåt annat än ett telefonnummer så tillåts det också).
Ytterligare ett testexempel Download testexempelmed en sparfil Download sparfilfinns.

Load och save (filformat):
Det är tillåtet att inte göra skillnad på alias och namn när man sparar till och laddar från fil. Filformatet är som följer: På varje rad i filen ska ett telefonnummer sparas först på raden, åtföljt av ett semikolon och sedan åtföljt av namnet som motsvarar telefonnumret fölt av semikolon. Om det alltså råkar finnas alias för namnet så sparar man detta på en egen rad, fast med samma telefonnummer. Vi får då en rad per namn i filen (ingen skillnad på "namn" och "alias"). Man behöver då inte ta hänsyn till alias när man sparar, vilket förenklar en hel del. När man laddar in en sådan fil (använder load) får man naturligtvis inte tillbaka aliasen, utan varje namn upptäder då i telefonboken som ett eget namn med eget telefonnummer (som råkar vara samma telefonnummer som någon anna, som tidigare var alias). Exempel (samma telefonbok som ovan):

123;Kalle;
123;Maria;
321;Anna;
321;Olle;

Internt i programmet är det lämpligt att använda ett dictionary som central datastruktur. Det finns dock all anledning att inte låta detta dictionary lagra telefonnummer direkt som värde, utan att blanda in muterbara datastrukturer (t ex objekt) som mellansteg (detta är den enklaste lösningen). Det är också starkt rekommenderat att inte göra någon skillnad överhuvudtaget på namn och alias; ett alias är bara ett till namn för samma nummer. Det interaktiva beteendet åstadkoms enklast genom att en loop (lämpligen while) börjar varje varv med att anropa input(), varefter resultatet analyseras och motsvarande kommando utförs (tänk på att detta inte går att göra rekursivt, eftersom vi potentiellt kör gopdtyckligt många varv, vilket skulle fylla upp minnet). Försök separera ut kommandon så att dessa implementeras i separata funktioner.
'''

class PhoneBook:
    def __init__(self):
        self.entries = {}  # name -> number

    def add(self, name, number):
        if name in self.entries:
            print(f"{name} already exists")
            return
        
        # Check if number already exists for a non-alias entry
        for existing_name, existing_number in self.entries.items():
            if existing_number == number:
                # If the existing name is an alias of the new name, it's fine
                # Otherwise, it's a duplicate number for a different person
                if not self._is_alias_of(existing_name, name):
                    print(f"{number} already exists")
                    return

        self.entries[name] = number
        print(f"Added {name} with number {number}")

    def _is_alias_of(self, name1, name2):
        # This is a simplified check. In a more robust system,
        # you'd have a way to group aliases. Here, we assume if they
        # share the same number, they are effectively aliases.
        return self.entries.get(name1) == self.entries.get(name2)

    def lookup(self, name):
        if name in self.entries:
            print(self.entries[name])
        else:
            print(f"{name} not found")

    def alias(self, name, newname):
        if name not in self.entries:
            print(f"{name} not found")
            return
        if newname in self.entries:
            print(f"{newname} already exists")
            return
        
        # If the newname already exists and has a different number, it's a conflict
        # If it exists and has the same number, it's already an alias, which is fine but we report it
        # The prompt implies "name not found or duplicate name" for alias,
        # so we'll treat existing newname as a duplicate name.
        
        self.entries[newname] = self.entries[name]
        print(f"Alias {newname} created for {name}")

    def change(self, name, new_number):
        if name not in self.entries:
            print(f"{name} not found")
            return
        
        # Check if the new_number already exists for a different, non-aliased entry
        for existing_name, existing_number in self.entries.items():
            if existing_number == new_number and not self._is_alias_of(existing_name, name):
                print(f"{new_number} already exists")
                return

        self.entries[name] = new_number
        print(f"Changed {name}'s number to {new_number}")

    def save(self, filename):
        try:
            with open(filename, 'w') as f:
                for name, number in self.entries.items():
                    f.write(f"{number};{name};\n")
            print(f"Phonebook saved to {filename}")
        except IOError:
            print(f"Error: Could not save to {filename}")

    def load(self, filename):
        self.entries = {} # Clear current phonebook
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(';')
                    if len(parts) >= 2:
                        number = parts[0]
                        name = parts[1]
                        self.entries[name] = number
            print(f"Phonebook loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
        except IOError:
            print(f"Error: Could not load from {filename}")

def main():
    phone_book = PhoneBook()
    prompt = "telebok> "

    while True:
        command_line = input(prompt).strip()
        parts = command_line.split()
        
        if not parts:
            continue

        command = parts[0].lower()

        if command == "add":
            if len(parts) == 3:
                phone_book.add(parts[1], parts[2])
            else:
                print("Usage: add <name> <number>")
        elif command == "lookup":
            if len(parts) == 2:
                phone_book.lookup(parts[1])
            else:
                print("Usage: lookup <name>")
        elif command == "alias":
            if len(parts) == 3:
                phone_book.alias(parts[1], parts[2])
            else:
                print("Usage: alias <name> <newname>")
        elif command == "change":
            if len(parts) == 3:
                phone_book.change(parts[1], parts[2])
            else:
                print("Usage: change <name> <new_number>")
        elif command == "save":
            if len(parts) == 2:
                phone_book.save(parts[1])
            else:
                print("Usage: save <filename>")
        elif command == "load":
            if len(parts) == 2:
                phone_book.load(parts[1])
            else:
                print("Usage: load <filename>")
        elif command == "quit":
            print("Exiting phonebook.")
            break
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()