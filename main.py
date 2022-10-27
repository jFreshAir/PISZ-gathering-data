# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# S pomočjo knjižnice sport-activities-features razčlenite podatke.

import os

directory = 'C:\\FERI\\PISZ\\Sport5\\1'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)

# Pridobite vsaj integralne metrike, podatke o hribih in jih združite glede na aktivnost (vsak šport naj
# ima eno izhodno datoteko glede na tip aktivnosti, ki združuje vse treninge z izbrano športno aktivnostji).
# Izhodna CSV datoteka naj vsebuje naslednje vsaj stolpce.
# ime_aktivnosti, id_sportnika, integralne_metrike (total duration, total_distance, calories...),
# podatke_o_hribih (num_hills, avg_altitude...)
# Primer ekstrakcije podatkov integralnih metrik s pomočjo knjižnice sport-activities-features:
# LINK

# Primer za ekstrakcije podatkov hribov s pomočjo knjižnice sport-activities-features:
# LINK

# Vizualizirajte podatke
# Z knjižnico sport-activities-features generirajte vsaj 2 grafa. Prav tako si izberite
# poljubno knjižnico za vizualizacijo podatkov v okolju Python, z izbrano knjižnico pripravite
# vsaj 4 smiselne grafe, ki prikazujejo prebrane podatke.
# Primeri knjižnic za vizualizacije podatkov v programskem jeziku Python
