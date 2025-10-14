
# python_tenta_traning.py
# Kodningsövningar som speglar en programmeringstenta i Python.
# Fyll i kod där det står TODO. Kör filen för att se tester och feedback.
# Kör:  python python_tenta_traning.py
# Du kan även köra:  python python_tenta_traning.py only 3    (kör bara uppgift 3)
# eller:             python python_tenta_traning.py only 3a   (kör bara del 3A)
#
# Viktigt: Jag har medvetet lagt in begränsningar (t.ex. inga listmetoder) i vissa uppgifter
# för att träna grundläggande logik. Följ docstrings noga.

from typing import List, Tuple, Any
import sys
import os

# ======= Liten testrigg =======
SKIP_TAGS = set()  # fylls dynamiskt via CLI

class SkipTest(Exception):
    pass

def _should_run(tag: str) -> bool:
    if not SKIP_TAGS:
        return True
    # Om SKIP_TAGS innehåller '3' körs alla 3x; om '3a' körs bara 3a
    return any(tag.startswith(t) for t in SKIP_TAGS)

def _eq(a, b):
    return a == b

def _assert_equal(got, expected, msg=""):
    if not _eq(got, expected):
        raise AssertionError(f"""FAIL
  got:      {got!r}
  expected: {expected!r}
  {msg}
""")

def _run_test(tag: str, func, *args, expected=None, check=None, msg=""):
    if not _should_run(tag):
        raise SkipTest(tag)
    try:
        res = func(*args)
    except NotImplementedError:
        print(f"[{tag}] SKIPPED (NotImplementedError)")
        return
    if check is not None:
        ok, extra = check(res)
        if not ok:
            raise AssertionError(f"""FAIL [{tag}]
  check failed: {extra}
""")
    elif expected is not None:
        _assert_equal(res, expected, f"[{tag}] {msg}")
    else:
        # no expectation
        print(f"[{tag}] OK (no expected value provided)")

def _banner(title: str):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

# ======= Uppgift 1 – Kontrollflöde & uttryck =======
def u1a_count_down(n: int) -> List[int]:
    """Returnera en lista med talen n, n-2, n-4, ... tills talet < 0.
    Ex: n=7 -> [7,5,3,1]
    Begränsning: använd while.
    """
    # TODO: skriv din kod här
    raise NotImplementedError

def u1b_toggle_case(s: str) -> str:
    """Returnera en ny sträng där bokstäver växlar versal/gemen
    med start som versal (första alfabetiska tecknet blir versal, nästa gemen osv).
    Endast a–z/A–Z påverkas. Övriga tecken bevaras och räknas inte med i växlingen.
    Ex: "hej, du!" -> "HeJ, dU!"
    Tips: använd .isalpha(), .upper(), .lower()
    """
    # TODO
    raise NotImplementedError

def _tests_u1():
    _banner("Uppgift 1 – Kontrollflöde & uttryck")
    _run_test("1a", u1a_count_down, 7, expected=[7,5,3,1])
    _run_test("1a", u1a_count_down, 0, expected=[])
    _run_test("1a", u1a_count_down, 1, expected=[1])
    _run_test("1b", u1b_toggle_case, "hej, du!", expected="HeJ, dU!")
    _run_test("1b", u1b_toggle_case, "A1b2C3", expected="A1b2C3")

# ======= Uppgift 2 – Debugga/förstå list-iteration =======
def u2_count_occ(lst: List[Any], e: Any) -> int:
    """Räkna förekomster av e i lst. Begränsning: använd for-loopen 'for x in lst:'."""
    # TODO
    raise NotImplementedError

def u2_fix_buggy_version(a: List[Any], target: Any) -> int:
    """Du får 'trasig' kod nedan (kommenterad). Rätta minimalt så att den fungerar
    med for-in-iteration (inte index-iteration).
    # def tally(a, target):
    #     hits=0
    #     for p in a:
    #         if a[p]==target:
    #             hits+=1
    #     return p
    """
    # TODO
    raise NotImplementedError

def _tests_u2():
    _banner("Uppgift 2 – Debugga/förstå list-iteration")
    _run_test("2", u2_count_occ, [1,2,2,3,2], 2, expected=3)
    _run_test("2", u2_count_occ, [], 99, expected=0)
    _run_test("2", u2_fix_buggy_version, ["a","b","a","a"], "a", expected=3)

# ======= Uppgift 3 – Listor: ny lista vs in-place & alias =======
def u3_repl_new(lst: List[int], old: int, new: int) -> List[int]:
    """Returnera NY lista där alla old ersätts av new. lst får ej ändras."""
    # TODO
    raise NotImplementedError

def u3_repl_inplace(lst: List[int], old: int, new: int) -> List[int]:
    """Modifiera lst PÅ PLATS. Returnera samma lista-objekt (alias). Använd while och index."""
    # TODO
    raise NotImplementedError

def u3_repl_copy_correct(lst: List[int], old: int, new: int) -> List[int]:
    """Skapa en ÄKTA kopia utan att använda slicing [:] eller list(...) eller copy().
    Tillåtna: len, range, append.
    """
    # TODO
    raise NotImplementedError

def _is_same_object(a, b):
    return id(a) == id(b)

def _tests_u3():
    _banner("Uppgift 3 – Listor & alias")
    L = [2,0,2,1]
    A = u3_repl_new(L, 2, 9)
    _run_test("3a", lambda: (L, A), expected=([2,0,2,1], [9,0,9,1]))
    _run_test("3a", lambda: _is_same_object(L, A), expected=False)

    L2 = [2,0,2,1]
    B = u3_repl_inplace(L2, 2, 9)
    _run_test("3b", lambda: (L2, B), expected=([9,0,9,1], [9,0,9,1]))
    _run_test("3b", lambda: _is_same_object(L2, B), expected=True)

    L3 = [2,0,2,1]
    C = u3_repl_copy_correct(L3, 2, 9)
    _run_test("3c", lambda: (L3, C), expected=([2,0,2,1], [9,0,9,1]))
    _run_test("3c", lambda: _is_same_object(L3, C), expected=False)

# ======= Uppgift 4 – Strängbygge utan metoder (förutom len/range/in) =======
def u4_build(s1: str, s2: str) -> str:
    """Antag len(s2)==3. Gå från vänster i s1:
    - Om tecknet matchar s2[0], lägg in hela s2 i resultatet.
    - Annars hoppa över tre tecken från s1 (eller allt som återstår om färre än tre).
    Begränsningar: använd inte andra strängmetoder än len/range/in.
    """
    # TODO
    raise NotImplementedError

def _tests_u4():
    _banner("Uppgift 4 – Strängbygge")
    _run_test("4", u4_build, "abxyczz", "abc", expected="abczz")
    _run_test("4", u4_build, "xxxx", "xqq", expected="xqq")
    _run_test("4", u4_build, "pqrs", "pqr", expected="pqr")

# ======= Uppgift 5 – Fil-I/O & undantag =======
def u5_readFloat(path: str) -> float:
    """Öppna fil och läs FÖRSTA raden som flyttal (float).
    Felhantering:
      - FileNotFoundError -> låt felet bubbla (dvs. du ska inte fånga det här)
      - ValueError om första raden inte går att tolka till float
    Fil ska stängas korrekt.
    """
    # TODO
    raise NotImplementedError

def _tests_u5():
    _banner("Uppgift 5 – Fil-I/O & undantag")
    # skapa testfiler
    base = os.path.join(os.path.dirname(__file__), "_u5_files")
    os.makedirs(base, exist_ok=True)
    good = os.path.join(base, "good.txt")
    bad  = os.path.join(base, "bad.txt")

    with open(good, "w", encoding="utf-8") as f:
        f.write("3.14\nresten ignorera")
    with open(bad, "w", encoding="utf-8") as f:
        f.write("hej\n42")

    # 5A: korrekt flyttal
    _run_test("5", u5_readFloat, good, expected=3.14)

    # 5A: ValueError på bad
    def check_bad(_):
        try:
            u5_readFloat(bad)
        except ValueError:
            return True, ""
        except NotImplementedError:
            raise
        except Exception as e:
            return False, f"fel typ: {type(e)}"
        return False, "borde kastat ValueError"
    _run_test("5", lambda: None, check=check_bad)

    # 5A: FileNotFoundError
    def check_no_file(_):
        try:
            u5_readFloat(os.path.join(base, "saknas.txt"))
        except FileNotFoundError:
            return True, ""
        except NotImplementedError:
            raise
        except Exception as e:
            return False, f"fel typ: {type(e)}"
        return False, "borde kastat FileNotFoundError"
    _run_test("5", lambda: None, check=check_no_file)

# ======= Uppgift 6 – Klassdesign =======
class Pair:
    """Representerar ett par tal.
    Krav:
      - __init__(self, a, b)
      - getPair(self) -> tuple
      - new(self) -> ny oberoende Pair med samma värden
      - absorb(self, other: Pair) -> gör self:s värden = others
    Extra: __repr__ och sum(self)
    """
    # TODO: implementera
    pass

def _tests_u6():
    _banner("Uppgift 6 – Klassdesign")
    # 1) init & getPair
    def check_init():
        p = Pair(2, 5)
        return p.getPair() == (2, 5)
    _run_test("6", lambda: check_init(), expected=True)

    # 2) new ger oberoende kopia
    def check_new():
        p1 = Pair(1, 2)
        p2 = p1.new()
        return (p1 is not p2) and (p1.getPair() == p2.getPair())
    _run_test("6", lambda: check_new(), expected=True)

    # 3) absorb
    def check_absorb():
        a = Pair(9, 9)
        b = Pair(3, 4)
        a.absorb(b)
        return a.getPair() == (3, 4)
    _run_test("6", lambda: check_absorb(), expected=True)

# ======= Uppgift 7 – Rekursion på två listor =======
def u7_g(ls1: List[int], ls2: List[int]) -> List[int]:
    """Returnera ny lista med:
      på index i: ls1[i]+ls2[i] om ls1[i] jämn, annars ls1[i]-ls2[i].
    Krav: ren rekursion (inga loopar). Anta lika långa listor.
    Tillåtna: len, slicing, + med listor för bygge av resultat.
    """
    # TODO
    raise NotImplementedError

def _tests_u7():
    _banner("Uppgift 7 – Rekursion")
    _run_test("7", u7_g, [3,2,2,5], [1,4,1,2], expected=[2,6,3,3])
    _run_test("7", u7_g, [], [], expected=[])

# ======= Bonus – Fällor =======
def bonus_mutable_default(x=[]):
    """Förstå vad som händer. Ändra inte signaturen. Implementera så att tests visar fallgroparna.
    Tips: x.append(1); return len(x)
    (Ja, denna får du *implementera* exakt som tipsrad)
    """
    # TODO
    raise NotImplementedError

def bonus_nested_alias(a: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    """Anta a är en lista av listor. Returnera (a, b) där b är en ytlig kopia (a[:]).
    Ändra b[0][1]=9 och returnera (a, b) för att illustrera aliasering.
    """
    # TODO
    raise NotImplementedError

def _tests_bonus():
    _banner("Bonus – Fällor")
    _run_test("B1", bonus_mutable_default, expected=1)
    _run_test("B1", bonus_mutable_default, expected=2)
    _run_test("B1", bonus_mutable_default, [], expected=1)
    _run_test("B1", bonus_mutable_default, expected=2)

    def check_alias(_):
        a = [[0,1],[2,3]]
        A, B = bonus_nested_alias(a)
        if A[0][1] != 9: return False, "a borde också ha 9 pga alias"
        if B[0][1] != 9: return False, "b borde ha 9"
        if id(A) == id(B): return False, "b ska vara annan lista-ytkopia"
        return True, ""
    _run_test("B2", lambda: None, check=check_alias)

# ======= Test-runner =======
def run_all_tests():
    for f in (_tests_u1, _tests_u2, _tests_u3, _tests_u4, _tests_u5, _tests_u6, _tests_u7, _tests_bonus):
        try:
            f()
        except SkipTest as st:
            print(f"[{st}] SKIPPED via -- only filter")

if __name__ == "__main__":
    # CLI: python file.py            -> kör allt
    #      python file.py only 3     -> kör bara uppgift 3 (3a, 3b, 3c)
    #      python file.py only 3a    -> kör bara 3a
    if len(sys.argv) >= 3 and sys.argv[1] == "only":
        SKIP_TAGS = set([sys.argv[2]])
        print(f"Kör endast taggar som börjar med: {sys.argv[2]!r}")
    else:
        SKIP_TAGS = set()
    run_all_tests()
    print("\nKlar. Implementera TODO-markeringarna för att få alla tester gröna.")
