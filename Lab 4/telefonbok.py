#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
En interaktiv telefonbok enligt labbspecen.

Stödjer:
- add name number
- lookup name
- alias name newname
- change name number
- save filename
- load filename
- quit

Egenskaper:
- Alla telefonnummer måste vara unika (förutom att alias delar samma nummer).
- Alias är helt likställda: fungerar i lookup/change/alias precis som originalnamnet.
- Felutskrifter matchar givna exempel.
- "save" sparar som återspelningsbara kommandorader (add/alias) som "load" kan läsa in.
- Endast en enkel prompt, ingen meny.
"""

from dataclasses import dataclass, field
from typing import Dict, Set, List, Optional
import sys
import shlex
import os

PROMPT = "phoneBook> "

@dataclass
class Group:
    number: str
    names: Set[str] = field(default_factory=set)

class PhoneBook:
    """
    Internt representerar vi telefonboken som alias-grupper:
      - name_to_gid: namn -> grupp-id
      - groups: gid -> Group(number, set(namn))
    Varje grupp har exakt ett telefonnummer som delas av alla dess alias.
    """
    def __init__(self) -> None:
        self.name_to_gid: Dict[str, int] = {}
        self.groups: Dict[int, Group] = {}
        self._next_gid: int = 1

    # --- Hjälpare ---

    def _number_in_other_group(self, number: str, gid: Optional[int]) -> bool:
        """True om numret används i en annan grupp än gid (eller någon grupp om gid=None)."""
        for gk, g in self.groups.items():
            if g.number == number and (gid is None or gk != gid):
                return True
        return False

    def _create_group(self, name: str, number: str) -> None:
        gid = self._next_gid
        self._next_gid += 1
        self.groups[gid] = Group(number=number, names={name})
        self.name_to_gid[name] = gid

    def _primary_name(self, gid: int) -> str:
        """Bestäm en stabil 'primär' (lexikografiskt minsta) för save-utskrift."""
        return sorted(self.groups[gid].names)[0]

    # --- Kommandon ---

    def cmd_add(self, name: str, number: str) -> None:
        if name in self.name_to_gid:
            print(f"{name} already exists")
            return
        if self._number_in_other_group(number, gid=None):
            print(f"{number} already exists")
            return
        self._create_group(name, number)

    def cmd_lookup(self, name: str) -> None:
        gid = self.name_to_gid.get(name)
        if gid is None:
            print(f"{name} not found")
            return
        print(self.groups[gid].number)

    def cmd_alias(self, name: str, newname: str) -> None:
        gid = self.name_to_gid.get(name)
        # Fel ska ges om name inte finns ELLER om newname redan finns (dubblettnamn)
        if gid is None or newname in self.name_to_gid:
            print("name not found or duplicate name")
            return
        # Lägg till nytt alias i samma grupp
        self.groups[gid].names.add(newname)
        self.name_to_gid[newname] = gid

    def cmd_change(self, name: str, number: str) -> None:
        gid = self.name_to_gid.get(name)
        if gid is None:
            print(f"{name} not found")
            return
        # Byta nummer: kolla att numret inte används i annan grupp
        if self._number_in_other_group(number, gid=gid):
            print(f"{number} already exists")
            return
        self.groups[gid].number = number

    def cmd_save(self, filename: str) -> None:
        """
        Sparar som kommandon (add + alias) som kan spelas upp av 'load'.
        Exempel:
          add Anna 123
          alias Anna Annika
        """
        lines: List[str] = []
        # Skriv grupper deterministiskt (sortera efter primärnamn)
        for gid in sorted(self.groups.keys(), key=lambda g: self._primary_name(g)):
            grp = self.groups[gid]
            names_sorted = sorted(grp.names)
            primary = names_sorted[0]
            lines.append(f"add {primary} {grp.number}")
            for alias_name in names_sorted[1:]:
                lines.append(f"alias {primary} {alias_name}")

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
                f.write("\n" if lines else "")
        except OSError:
            # Specen kräver inte särskild feltext, så var tyst vid misslyckande
            pass

    def cmd_load(self, filename: str) -> None:
        """
        Läser in fil sparad av 'save'. Telefonboken i minnet kastas bort
        och ersätts helt av filens innehåll.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().splitlines()
        except OSError:
            # Specen kräver inte felmeddelande här; vi förblir tysta
            content = []

        # Bygg en NY tom bok och spela upp raderna i den
        new_book = PhoneBook()
        for raw in content:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            # Kör endast de tillåtna kommandona (add/alias/change tillåts om de finns)
            parts = _split_command(line)
            if not parts:
                continue
            cmd = parts[0].lower()
            if cmd == "add" and len(parts) >= 3:
                new_book.cmd_add(parts[1], parts[2])
            elif cmd == "alias" and len(parts) >= 3:
                new_book.cmd_alias(parts[1], parts[2])
            elif cmd == "change" and len(parts) >= 3:
                new_book.cmd_change(parts[1], parts[2])
            # Ignorera andra rader tyst

        # Ersätt aktuell bok med den nya
        self.name_to_gid = new_book.name_to_gid
        self.groups = new_book.groups
        self._next_gid = new_book._next_gid


def _split_command(line: str) -> List[str]:
    """
    Dela upp kommandoraden till ord. Vi använder shlex.split för robust whitespace-hantering.
    (Specen kräver att ett eller flera whitespace accepteras.)
    """
    try:
        # shlex låter oss t.ex. skriva "add 'Anna-Lena' 123" om man vill.
        return shlex.split(line)
    except ValueError:
        # Ogiltig quoting -> returnera tom lista så kommandot ignoreras
        return []


def process_line(pb: PhoneBook, line: str) -> bool:
    """
    Behandla en rad. Returnerar False om vi ska avsluta (quit), annars True.
    """
    parts = _split_command(line)
    if not parts:
        return True

    cmd = parts[0].lower()

    # --- Kommandon enligt spec ---
    if cmd == "add":
        if len(parts) >= 3:
            pb.cmd_add(parts[1], parts[2])
        else:
            # Specen kräver ingen särskild feltext här; ignorera eller skriv minimal hjälp om så önskas
            pass
    elif cmd == "lookup":
        if len(parts) >= 2:
            pb.cmd_lookup(parts[1])
        else:
            pass
    elif cmd == "alias":
        if len(parts) >= 3:
            pb.cmd_alias(parts[1], parts[2])
        else:
            # I exemplet används specifik feltext endast för (name saknas / dubblettnamn)
            print("name not found or duplicate name")
    elif cmd == "change":
        if len(parts) >= 3:
            pb.cmd_change(parts[1], parts[2])
        else:
            pass
    elif cmd == "save":
        if len(parts) >= 2:
            pb.cmd_save(parts[1])
        else:
            pass
    elif cmd == "load":
        if len(parts) >= 2:
            pb.cmd_load(parts[1])
        else:
            pass
    elif cmd == "quit":
        return False
    else:
        # Okänt kommando -> specen kräver ingen särskild text; vi tiger
        pass

    return True


def main() -> None:
    pb = PhoneBook()
    # Interaktiv loop
    while True:
        try:
            # Endast prompt, ingen meny
            line = input(PROMPT)
        except EOFError:
            # Ctrl-D avslutar också
            break
        except KeyboardInterrupt:
            # Ctrl-C -> ny rad + fortsätt
            print()
            continue

        if not process_line(pb, line):
            break


if __name__ == "__main__":
    main()
