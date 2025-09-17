""" Uppgift 5: En numerisk ekvationslösare
I den här labben ska vi implementera en numerisk ekvationslösare. Vi ska alltså, steg för steg, göra ett program som kan lösa ekvationer numeriskt. Den matematiska förståelsen (läs i bakgrundsinformation) för en ekvationslösare är inte kritisk, men gör uppgiften betydligt intressantare.
Newton-raphsons metod är en iterativ metod (man hittar bättre och bättre approximationer) för att hitta nollställen. Betrakta följande bild:
grafisk illustration av nntwon-raphsons metod.
Vi börjar med att gissa att x1 är nollställe. Därefter drar vi en tangent från funktionen i ner till x-axeln och får en ny, bättre, gissning, x2, osv... För att kunna ta ut tangenten till funktionen behöver vi funktionens derivata, eller iallafall en skattning av derivatan. Detta leder oss in på uppgift 5a:

Uppgift 5a
En funktions derivata i en punkt kan skattas genom att använda lutningen av en linje mellan två närliggande punkter som skattning. Betrakta följande bild:
derivata.png

Skriv en Python-funktion derivative som returnerar lutningen (första derivatan) för funktionen f i punkten x. Den exakta lutningen kan (förstås) bara fås om vi vet den exakta definitionen av f, men vi kan åstadkomma en bra approximation genom att titta lite vid sidan av punkten x och se hur mycket f(x) förändras. Hur mycket vid sidan om vi ska titta ska bestämmas av en tredje parameter h.

Alltså: implementera funktionen derivative(f, x, h), och returnera resultatet som ett flyttal. För den som inte vill reda ut matematiken för approximation av lutningen själv kan följande formel för resultatet användas:

eq8.jpg

Notera: Vår funktion derivative som vi här ska skriva kommer att ta en annan funktion f som parameter. En sådan konstruktion brukar betecknas som mycket avancerad i många andra programmeringsspråk, men icke så i Python! Skriv bara argumentlistan på vanligt sätt, och anropa f ifrån derivative där så önskas. Att den faktiska betydelsen av f i detta läge är okänd är inte konstigare än att parametern x också är det. När derivative ska anropas (t ex vid testning) ska den önskade funktionen skickas med som argument. Exempel: om vi vill beräkna lutningen av funktionen math.sin i punkten math.pi  skriver vi derivative(math.sin, math.pi, 0.0001).

Testa din deriveringsfunktion på åtminstone tre olika konkreta flyttalsfunktioner, i punkter där du redan vet vad lutningen ska vara. Dina tre funktioner implementerar du som funktioner i python, helt enkelt.

Uppgift 5b
Implementera en numerisk ekvationslösare solve(f, x0, h) enligt Newton-Raphsons metod . Parametern f är den funktion vars nollställe söks, x0 är sökningens startvärde och h den önskade noggrannheten. Resultatet ska vara ett flyttal.

Enligt Newton-Raphsons metod kan nästa approximation (index n+1) beräknas ur den föregående (index n) enligt formeln

eq9.jpg

där notationen f '  betyder just lutningen för funktionen f . Det är alltså meningen att derivative från deluppgift 1 ska användas här. Det tredje argumentet till derivative väljs lämpligen att vara lika med ekvationslösarens noggrannhet h.

Ekvationslösaren ska implementeras med hjälp av en snurra (loop). Observera att antalet varv i snurran (loopen) inte är förutbestämt, utan beroende på de aktuella parametervärden. Den egentliga konsten i denna uppgift är att tolka hur formeln för approximationer ovan ska konkretiseras i termer av Python-variabler och multipel tilldelning. Ett lämpligt villkor för att sluta iterera (loopa), är att om skillnaden i x-led mellan två iterationer är mindre än h så är beräkningen klar. Observera att skillnaden då alltså kan vara både positiv och negativ. Det är viktigt (krav) att programmet alltid terminerar om beräkningen har konvergerat (detta betyder att om värdet "ligger still" (x inte ändrar sig), så att säga, så måste programmet sluta, och detta testar man genom att se om x ändrar sig).

Extra information för den intresserade:
Notera: Eftersom en funktion kan ha flera nollställen krävs det ibland också lite tankemöda bakom valet av x0, men det är inget som påverkar hur ekvationslösaren implementeras i sig. Ej heller kräver vi att ekvationslösaren hanterar de fall då lösningar saknas, dessa kommer i stället att ge sig till känna genom att ekvationslösaren inte terminerar. (Fråga att fundera på: hur vet vi att ett program verkligen inte kommer att terminera, och inte bara tar väldigt lång tid på sig?)

Slutligen bryr vi oss inte heller om det faktum att flyttalrepresentation ofta innebär en viss avrundning i sig. Den stora utmaningen vid användning av numeriska metoder är annars att avgöra i vilken omfattning successiva avrundningsfel påverkar resultatets noggrannhet.

Testa din ekvationslösare på åtminstone tre olika konkreta flyttalsfunktioner för vilka du känner till alla nollställen analytiskt och kan välja rimligt startvärde. Exempel på testfunktioner är:

x2-1=0 (nollställe vid x=1 och x=-1, vilket startvärde som helst borde funka)
2x-1=0 (nollställe vid x=0, de flesta startvärden borde gå bra)

Testa också att numeriskt lösa ekvationen

eq10.jpg

Denna ekvation har den egenskapen att den inte kan lösas analytiskt (prova gärna!). """


import math


print("\n5a:")

# 5a   
def derivata(f, x, h):
    approx = (f(x + h) - f(x - h)) / (2 * h)        # Matematiska formeln för derivata
                                                 
    return approx

# Kör koden med funktionen f = sin, x = pi, och steglängden h = 0.001
print("sin test:", derivata(math.sin, math.pi, 0.001), "=", math.cos(math.pi))


print("\n5b:")


# 5b
def solve(f, x0, h):
    x = x0
    while True:
        d = derivata(f, x, h)      
        if d == 0:                   
            return None
        x_new = x - f(x) / d         
        if abs(x_new - x) < h:       
            return x_new
        x = x_new

# Test
def f1(x): 
    return x**2 - 1
def f2(x): 
    return 2*x - 1
def f3(x): 
    return math.cos(x) - x

print("solve x^2-1=0, start=2:", solve(f1, 2, 1e-6))
print("solve 2x-1=0, start=0:", solve(f2, 0, 1e-6))
print("solve cos(x)-x=0, start=1:", solve(f3, 1, 1e-6))



