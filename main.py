# S pomočjo knjižnice sport-activities-features razčlenite podatke.

import os
import re
import pickle
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.topographic_features import TopographicFeatures
from sport_activities_features.plot_data import PlotData


directory = 'C:\\FERI\\PISZ\\Sport5\\1'
tcx_file = TCXFile()


# Pridobite vsaj integralne metrike, podatke o hribih in jih združite glede na aktivnost (vsak šport naj
# ima eno izhodno datoteko glede na tip aktivnosti, ki združuje vse treninge z izbrano športno aktivnostji).

all_results = []
all_activities = []
def SaveResultArrayPickle(result):

    #preveri pravilnost oblike rezultata
    if(type(result) is not dict):
        print("The result must be a dictionary!")
        return
    #dodaja nove vrste aktivnosti
    for type in all_activities:
        if(result['activity_type'] == type):
            continue
        else:
            all_activities.append(result['activity_type'])

    #shrani rezultat v polje in datoteko
    all_results.append(result)
    #pickle
    file = open('C:\FERI\PISZ\processedData.pickle', "wb")
    pickle.dump(all_results, file)
    file.close()

def foo():
    a = "tunekajpiše"
    b = "to je naslednja vrstica"

    f = open("C:\\FERI\\PISZ\\" + 'neke' + ".txt", 'a')
    f.write(a + "\n")
    f.write(b)

def SortByType():
    for result in all_results:
        type = result['activity_type']
        f = open('C:\\FERI\\PISZ\\SportDataByType\\' + type + '.csv', 'a')
        f.write(result)
        f.close()


def ReadFiles():
    try:
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):

                id = os.path.splitext(filename)[0]
                print(id)

                integralMetrics = tcx_file.extract_integral_metrics(f)
                #print(integralMetrics)

                data = tcx_file.read_one_file(f)
                #print(data.keys())
                hill = HillIdentification(data['altitudes'])
                hill.identify_hills()
                allHills = hill.return_hills()
                Top = TopographicFeatures(allHills)
                num = Top.num_of_hills()
                avg = Top.avg_altitude_of_hills(data['altitudes'])
                avgAscent = Top.avg_ascent_of_hills(data['altitudes'])
                distance_hills = Top.distance_of_hills(data['positions'])

                single_result = {
                    "id": id,
                    "activity_type": data['activity_type'],
                    "intregral_metrics": integralMetrics,
                    "hill_data": Top
                }

                print(single_result)
                SaveResultArrayPickle(single_result)
    except:
        print("Error, file " + filename)


#ReadFiles()
#foo()

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
