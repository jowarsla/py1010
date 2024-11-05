"""
@author: Jorunn Warsla
Svar på arbeidskrav 1 i PY1010 ved USN 2024 HØST-2025 VÅR.
Kostnader som renter på billån og verditap
er ikke tatt med i regnestykket, da de antas
å være like for elbil og bensinbil.
"""

"""
Brukt for debug
antallKM = int(input("Hvor mange km kjører du pr år? \n"))  # Spør om input fra bruker, bruker må taste inn antall kjørte km pr år
"""

# Definerer variabler
antallKM = 20000  # Antall kjørte km pr år
forsikringBe = 7500  # Forsikring bensinbil: Kr pr år
forsikringEl = 5000  # Forsikring elbil: Kr pr år
trafikkAvg = 8.38*365  # Trafikkavgift pr år: Kr pr dag * 365 dager i et år
drivstoffBe = 1*antallKM  # Drivstofforbruk bensinbil pr år: Kr pr km * antall kjørte km pr år
drivstoffEl = (0.2*2.00)*antallKM  # Drivstofforbruk elbil pr år: Kr pr km * antall kjørte km pr år
bomavgBe = 0.3*antallKM  # Bomavgift bensinbil pr år: Kr pr km * antall kjørte km pr år
bomavgEl = 0.1*antallKM  # Bomavgift elbil pr år: Kr pr km * antall kjørte km pr år

# Utregning
kost_bensinbil = float(forsikringBe + trafikkAvg + drivstoffBe + bomavgBe)  # Regner ut årlig kostnad alle utgifter bensinbil
kost_elbil = float(forsikringEl + trafikkAvg + drivstoffEl + bomavgEl)  # Regner ut årlig kostnad alle utgifter elbil

"""
Brukt for debug
print()  # Printer tom linje
info =  str("Kostnader som renter på billån og verditap er ikke tatt med i regnestykket, da de antas å være like for elbil og bensinbil.")
print(info)  # Printer infotekst
print()  # Printer tom linje
bensinbil = f"Oversikt kostnader bensinbil:\nForsikring: {forsikringBe:.2f} kr.\nTrafikkavgift: {trafikkAvg:.2f} kr.\nDrivstoffutgifter: {drivstoffBe:.2f} kr.\nBomavgifter: {bomavgBe:.2f} kr."
print(bensinbil)  # Skriver ut alle årlige kostnader for bensinbil
"""

print("Årlige kostnader bensinbil:",  "{:.2f}".format(kost_bensinbil), "kr.")  # Printer ut årlig kostnad alle utgifter bensinbil

"""
Brukt for debug
print()  # Printer tom linje
elbil = f"Oversikt kostnader elbil: \nForsikring: {forsikringEl:.2f} kr.\nTrafikkavgift: {trafikkAvg:.2f} kr.\nDrivstoffutgifter: {drivstoffEl:.2f} kr.\nBomavgifter: {bomavgEl:.2f} kr."
print(elbil)  # Skriver ut alle årlige kostnader for elbil
"""

print("Årlige kostnader elbil:",  "{:.2f}".format(kost_elbil), "kr.")  # Printer ut årlig kostnad alle utgifter elbil

#print()  # Printer tom linje
z = kost_bensinbil - kost_elbil  # Regner ut differansen mellom årlige konstader bensinbil og elbil
print("Differansen i årlige kostnader for bensinbil og elbil er:", "{:.2f}".format(z), "kr.")  # Printer ut differansen mellom årlige konstader bensinbil og elbil