"""
@author: Jorunn Warsla
Svar på arbeidskrav 2 i PY1010 ved USN 2024 HØST-2025 VÅR.
"""



print("\n@author: Jorunn Warsla")
print("Svar på arbeidskrav 2 i PY1010 ved USN 2024 HØST-2025 VÅR\n\n")



"""
Oppg 1)
Du skal her lage et program som skal starter med alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024
og skrive svaret til skjerm med passende tekst.
"""

print("Oppgave 1:")
alder = int(input("Hvilket år er du født? "))
arstall = 2024
print("I løpet av 2024 fylte du", arstall-alder, "år.")
print("\n")



"""
Oppg 2)
Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)? 
"""

print("Oppgave 2:")
from math import ceil
antall_elever = int(input("Skriv inn antall elever: "))
antall_pizza = float(antall_elever*0.25)
print("Det må handles inn", ceil(antall_pizza), "pizzaer til festen.")
print("\n")



"""
Oppg 3)
Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
"""

print("Oppgave 3:")
import numpy as np
v_grad = float(input("Skriv inn gradtallet: "))
v_rad = float(v_grad*np.pi/180)
print("Radiantallet er: ", round(v_rad, 2))
print("\n")



"""
Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.
b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London
c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm
data = {
	"Norge": ["Oslo", 0.634],
	"England": ["London", 8.982],
	"Frankrike": ["Paris", 2.161],
	"Italia": ["Roma", 2.873],
	}
"""

print("Oppgave 4a:")
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873],
        }
for x in data:
    print(x)
print("\n")
print("Oppgave 4b:")
land = input("Velg et land fra listen: ")
if land in data:
    hovedstad, ant_innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land}, og det er {ant_innbyggere} millioner innbyggere i {hovedstad}.")
else:
    print(f"{land} finnes ikke i dictionarien.")
print("\n")
print("Oppgave 4c:")
nytt_land = input("Legg til et nytt land: ")

if nytt_land in data:
    print(f"{nytt_land} finnes allerede i dictionarien.")
else:
    hovedstad = input("Oppgi hovedstad: ")
    ant_innbyggere = float(input("Oppgi antall innbyggere: "))

data[nytt_land] = [hovedstad, ant_innbyggere]
print(data)
print("\n")



"""
Oppg 5)
Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst. 
"""

print("Oppgave 5:")
import numpy as np

def func_beregn(a, b):
    hypotenusen = np.sqrt(a**2 + b**2)
    areal_trekant = (a*b)/2
    radius = a/2
    
    areal_halvsirkel = ((np.pi*radius**2)/2)
    
    total_areal = areal_trekant + areal_halvsirkel
    
    omkrets_trekantToSider = b + hypotenusen
    omkrets_halvsirkel = ((2*np.pi*radius)/2)
    
    total_omkrets = omkrets_trekantToSider + omkrets_halvsirkel
    
    return total_areal, total_omkrets

a = float(input("Skriv inn lengden på kortside a: "))
b = float(input("Skriv inn lengden på langside b: "))

areal, omkrets = func_beregn(a, b)

print("Arealet til figuren er ", areal)
print("Omkretsen til figuren er", omkrets)
print("\n")



"""
Oppg 6)
Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].
"""

print("Oppgave 6:")
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)
y = f(x)

plt.title("Plott av funksjonen f(x)=x^2-5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.plot(x, y)