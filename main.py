# S pomočjo knjižnice sport-activities-features razčlenite podatke.

import os
import re
import csv
import pickle

import numpy
import pandas as pd
import seaborn as sns
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.topographic_features import TopographicFeatures
from sport_activities_features.plot_data import PlotData
from sport_activities_features.interval_identification import (
    IntervalIdentificationByHeartRate,
    IntervalIdentificationByPower,
)

storedData = pd.read_pickle('C:\FERI\PISZ\processedData.pickle')
data_frame = pd.DataFrame(data=storedData)

def minMaxMeanMedianColumns():
    print("MAX VALUE OF COLUMNS")
    print("")
    print(data_frame.max(axis=0)['distance'])
    print(data_frame.max(axis=0)['duration'])
    print(data_frame.max(axis=0)['calories'])
    print(data_frame.max(axis=0)['hr_avg'])
    print(data_frame.max(axis=0)['hr_max'])
    print(data_frame.max(axis=0)['hr_min'])
    print(data_frame.max(axis=0)['altitude_avg'])
    print(data_frame.max(axis=0)['altitude_max'])
    print(data_frame.max(axis=0)['altitude_min'])
    print(data_frame.max(axis=0)['ascent'])
    print(data_frame.max(axis=0)['descent'])
    print(data_frame.max(axis=0)['steps'])
    print(data_frame.max(axis=0)['num_of_hills'])
    print(data_frame.max(axis=0)['avg_altitude'])
    print(data_frame.max(axis=0)['avg_ascent'])
    print(data_frame.max(axis=0)['distance_hills'])
    print(data_frame.max(axis=0)['hills_share'])

    print("")
    print("")

    print("MIN VALUE OF COLUMNS")
    print("")
    print(data_frame.min(axis=0)['distance'])
    print(data_frame.min(axis=0)['duration'])
    print(data_frame.min(axis=0)['calories'])
    print(data_frame.min(axis=0)['hr_avg'])
    print(data_frame.min(axis=0)['hr_max'])
    print(data_frame.min(axis=0)['hr_min'])
    print(data_frame.min(axis=0)['altitude_avg'])
    print(data_frame.min(axis=0)['altitude_max'])
    print(data_frame.min(axis=0)['altitude_min'])
    print(data_frame.min(axis=0)['ascent'])
    print(data_frame.min(axis=0)['descent'])
    print(data_frame.min(axis=0)['steps'])
    print(data_frame.min(axis=0)['num_of_hills'])
    print(data_frame.min(axis=0)['avg_altitude'])
    print(data_frame.min(axis=0)['avg_ascent'])
    print(data_frame.min(axis=0)['distance_hills'])
    print(data_frame.min(axis=0)['hills_share'])

    print("")
    print("")

    print("MEAN VALUE OF COLUMNS")
    print("")
    print(data_frame['distance'].mean())
    print(data_frame['duration'].mean())
    print(data_frame['calories'].mean())
    print(data_frame['hr_avg'].mean())
    print(data_frame['hr_max'].mean())
    print(data_frame['hr_min'].mean())
    print(data_frame['altitude_avg'].mean())
    print(data_frame['altitude_max'].mean())
    print(data_frame['altitude_min'].mean())
    print(data_frame['ascent'].mean())
    print(data_frame['descent'].mean())
    print(data_frame['steps'].mean())
    print(data_frame['num_of_hills'].mean())
    print(data_frame['avg_altitude'].mean())
    print(data_frame['avg_ascent'].mean())
    print(data_frame['distance_hills'].mean())
    print(data_frame['hills_share'].mean())

    print("")
    print("")

    print("MEDIAN VALUE OF COLUMNS")
    print("")
    print(data_frame['distance'].median())
    print(data_frame['duration'].median())
    print(data_frame['calories'].median())
    print(data_frame['hr_avg'].median())
    print(data_frame['hr_max'].median())
    print(data_frame['hr_min'].median())
    print(data_frame['altitude_avg'].median())
    print(data_frame['altitude_max'].median())
    print(data_frame['altitude_min'].median())
    print(data_frame['ascent'].median())
    print(data_frame['descent'].median())
    print(data_frame['steps'].median())
    print(data_frame['num_of_hills'].median())
    print(data_frame['avg_altitude'].median())
    print(data_frame['avg_ascent'].median())
    print(data_frame['distance_hills'].median())
    print(data_frame['hills_share'].median())

    print("")
    print("")

def missingNumberColumns():
    print("SUM OF MISSING NUMBERS")
    print("")
    print(data_frame['distance'].isna().sum())
    print(data_frame['duration'].isna().sum())
    print(data_frame['calories'].isna().sum())
    print(data_frame['hr_avg'].isna().sum())
    print(data_frame['hr_max'].isna().sum())
    print(data_frame['hr_min'].isna().sum())
    print(data_frame['altitude_avg'].isna().sum())
    print(data_frame['altitude_max'].isna().sum())
    print(data_frame['altitude_min'].isna().sum())
    print(data_frame['ascent'].isna().sum())
    print(data_frame['descent'].isna().sum())
    print(data_frame['steps'].isna().sum())
    print(data_frame['num_of_hills'].isna().sum())
    print(data_frame['avg_altitude'].isna().sum())
    print(data_frame['avg_ascent'].isna().sum())
    print(data_frame['distance_hills'].isna().sum())
    print(data_frame['hills_share'].isna().sum())

    print("")
    print("")


tcx_file2 = TCXFile()
directory2 = 'C:\\FERI\\PISZ\\Sport5\\1'
all_power = []
all_heart_rate = []

num_of_int_pw = []
min_duration = []
max_duration = []
avg_duration = []
min_distance = []
max_distance = []
avg_distance = []

num_of_int_hr = []
min_duration_interval = []
max_duration_interval = []
avg_duration_interval = []
min_distance_interval = []
max_distance_interval = []
avg_distance_interval = []
min_heartrate_interval = []
max_heartrate_interval = []
avg_heartrate_interval = []

def intervalIdentification():
    i = 0
    err = 0
    err_pow = 0
    err_hr = 0
    for filename in os.listdir(directory2):
        i += 1
        print(i)
        try:
            if i > 250:
                return

            if i == 201:
                continue

            f = os.path.join(directory2, filename)
            if os.path.isfile(f):
                data = tcx_file2.read_one_file(f)

                try:
                    intervals_pw = IntervalIdentificationByPower(data['distances'],
                                                                 data['timestamps'],
                                                                 data['altitudes'],
                                                                 mass=70)
                    intervals_pw.identify_intervals()
                    statistics_power = intervals_pw.calculate_interval_statistics()
                    # all_intervals = intervals_pw.return_intervals()

                    #all_power.append(statistics_power)
                    num_of_int_pw.append(statistics_power['number_of_intervals'])
                    min_duration.append(statistics_power['min_duration'])
                    max_duration.append(statistics_power['max_duration'])
                    avg_duration.append(statistics_power['avg_duration'])
                    min_distance.append(statistics_power['min_distance'])
                    max_distance.append(statistics_power['max_distance'])
                    avg_distance.append(statistics_power['avg_distance'])

                except:
                    print("Error POWER")
                    #all_power.append(None)
                    num_of_int_pw.append(None)
                    min_duration.append(None)
                    max_duration.append(None)
                    avg_duration.append(None)
                    min_distance.append(None)
                    max_distance.append(None)
                    avg_distance.append(None)
                    err_pow += 1

                try:
                    intervals_hr = IntervalIdentificationByHeartRate(data['distances'],
                                                                     data['timestamps'],
                                                                     data['altitudes'],
                                                                     data['heartrates'])
                    intervals_hr.identify_intervals()
                    statistics_hr = intervals_hr.calculate_interval_statistics()
                    # all_intervals_hr = intervals_hr.return_intervals()

                    #all_heart_rate.append(statistics_hr)
                    #print(statistics_hr)

                    num_of_int_hr.append(statistics_hr['number_of_intervals'])
                    min_duration_interval.append(statistics_hr['min_duration_interval'])
                    max_duration_interval.append(statistics_hr['max_duration_interval'])
                    avg_duration_interval.append(statistics_hr['avg_duration_interval'])
                    min_distance_interval.append(statistics_hr['min_distance_interval'])
                    max_distance_interval.append(statistics_hr['max_distance_interval'])
                    avg_distance_interval.append(statistics_hr['avg_distance_interval'])
                    min_heartrate_interval.append(statistics_hr['min_heartrate_interval'])
                    max_heartrate_interval.append(statistics_hr['max_heartrate_interval'])
                    avg_heartrate_interval.append(statistics_hr['avg_heartrate_interval'])

                except:
                    print("Error HEART RATE")
                    #all_heart_rate.append(None)
                    num_of_int_hr.append(None)
                    min_duration_interval.append(None)
                    max_duration_interval.append(None)
                    avg_duration_interval.append(None)
                    min_distance_interval.append(None)
                    max_distance_interval.append(None)
                    avg_distance_interval.append(None)
                    min_heartrate_interval.append(None)
                    max_heartrate_interval.append(None)
                    avg_heartrate_interval.append(None)
                    err_hr += 1

        except:
            print("Error with intervals")
            err += 1


def addIntervalColumns():
    data_frame['num_of_intervals_pw'] = num_of_int_pw
    data_frame['min_duration'] = min_duration
    data_frame['max_duration'] = max_duration
    data_frame['avg_duration'] = avg_duration
    data_frame['min_distance'] = min_distance
    data_frame['max_distance'] = max_distance
    data_frame['avg_distance'] = avg_distance

    data_frame['num_of_intervals_hr'] = num_of_int_hr
    data_frame['min_duration_interval'] = min_duration_interval
    data_frame['max_duration_interval'] = max_duration_interval
    data_frame['avg_duration_interval'] = avg_duration_interval
    data_frame['min_distance_interval'] = min_distance_interval
    data_frame['max_distance_interval'] = max_distance_interval
    data_frame['avg_distance_interval'] = avg_distance_interval
    data_frame['min_heartrate_interval'] = min_heartrate_interval
    data_frame['max_heartrate_interval'] = max_heartrate_interval
    data_frame['avg_heartrate_interval'] = avg_heartrate_interval


def deleteColumnISNA(new_data_frame):
    max_missing = new_data_frame.isna().sum().max()
    column = new_data_frame.columns[new_data_frame.isna().sum() == max_missing]
    print("NAJVEČ MANJKAJOČIH PODATKOV IMA STOLPEC:")
    print(column._values)
    print(max_missing)
    print("")
    min_required_data = len(new_data_frame) - max_missing + 1

    print(new_data_frame)
    new_data_frame = new_data_frame.dropna(axis='columns', thresh=min_required_data)
    print(new_data_frame)
    return new_data_frame


def normalization(data_frame):
    copy_frame = data_frame.copy()


    copy_frame['avg_distance'] = (copy_frame['avg_distance'] - copy_frame['avg_distance'].min()) / (copy_frame['avg_distance'].max() - copy_frame['avg_distance'].min())

    print("ORIGINAL")
    print(data_frame['avg_distance'])
    print("NORMALIZIRANO")
    print(copy_frame['avg_distance'])

    return copy_frame


def discretisize(data_frame):
    print("ORIGINAL")
    print(data_frame['num_of_hills'])

    data_frame['discretisized1'] = numpy.digitize(data_frame['num_of_hills'],
                                                  numpy.array([0.0, 2.5, 7.5, 10.0]))
    print("DISKRETIZIRANO")
    print(data_frame['discretisized1'])

    return data_frame


def allCategories():
    print(data_frame['activity_type'].unique())


def task2():
    minMaxMeanMedianColumns()
    missingNumberColumns()
    allCategories()
    # print(data_frame)

    intervalIdentification()
    addIntervalColumns()
    data_frame.to_pickle('C:\\FERI\\PISZ\\addedIntervalsData.pickle')

    newStoredData = pd.read_pickle('C:\\FERI\\PISZ\\addedIntervalsData.pickle')
    new_data_frame = pd.DataFrame(data=newStoredData)

    new_data_frame = deleteColumnISNA(new_data_frame)
    new_data_frame = normalization(new_data_frame)
    new_data_frame = discretisize(new_data_frame)

    #new_data_frame.to_csv('C:\FERI\PISZ\SportDataByType\AllNewData.csv')

    # print("št v POWER")
    # print(len(num_of_int_pw))
    # print("št v HEARTRATE")
    # print(len(num_of_int_hr))
    # print("random check")
    # print(len(avg_distance))
    # print(avg_distance)




task2()















all_results = []
all_activities = []
def SaveResultArrayPickle(result):

    #preveri pravilnost oblike rezultata
    if(type(result) is not dict):
        print("The result must be a dictionary!")
        return

    #prva iteracija
    if(len(all_activities) == 0):
        all_activities.append(result['activity_type'])
        #print("prva dodana")

    #dodaja nove vrste aktivnosti
    if result['activity_type'] in all_activities:
        print("")
    else:
        all_activities.append(result['activity_type'])
        print("Nov tip dodan")

    #shrani rezultat v polje in datoteko
    all_results.append(result)
    #pickle
    file = open('C:\FERI\PISZ\processedData.pickle', "wb")
    pickle.dump(all_results, file)
    file.close()

#def foo():
 #   a = "tunekajpiše"
  #  b = "to je naslednja vrstica"
#
 #   f = open("C:\\FERI\\PISZ\\" + 'neke' + ".txt", 'a')
  #  f.write(a + "\n")
   # f.write(b)

#gres cez vse podatke, int steje pozicijo arraya,
def SortAndWriteCSV():

    array_of_act_arrays = []
    for x in all_activities:
        single_array = []
        array_of_act_arrays.append(single_array)

    for result in all_results:
        ac_type = result['activity_type']
        array_of_act_arrays[all_activities.index(ac_type)].append(result)

    keys = all_results[0].keys()
    for array in array_of_act_arrays:
        with open('C:\\FERI\\PISZ\\SportDataByType\\' + array[0]['activity_type']
                  + '.csv', 'w', newline='')as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(array)

        #f = open('C:\\FERI\\PISZ\\SportDataByType\\' + ac_type + '.csv', 'a')
        #f.write(result)
        #f.close()




tcx_file = TCXFile()
directory = 'C:\\FERI\\PISZ\\Sport5\\1'
def ReadFiles():
    i = 0
    for filename in os.listdir(directory):
        i += 1
        print(i)
        try:
            if i > 250:
                return

            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                id = os.path.splitext(filename)[0]
                #print(id)

                integralMetrics = tcx_file.extract_integral_metrics(f)
                #print(integralMetrics)

                data = tcx_file.read_one_file(f)
                #print(data.keys())
                hill = HillIdentification(data['altitudes'])
                hill.identify_hills()
                allHills = hill.return_hills()
                Top = TopographicFeatures(allHills)
                numhills = Top.num_of_hills()
                avg = Top.avg_altitude_of_hills(data['altitudes'])
                avgAscent = Top.avg_ascent_of_hills(data['altitudes'])
                distance_hills = Top.distance_of_hills(data['positions'])
                hills_share = Top.share_of_hills(distance_hills, data['total_distance'])

                single_result = {
                    "id": id,
                    "activity_type": data['activity_type'],
                    "distance": integralMetrics['distance'],
                    "duration": integralMetrics['duration'],
                    "calories": integralMetrics['calories'],
                    "hr_avg": integralMetrics['hr_avg'],
                    "hr_max": integralMetrics['hr_max'],
                    "hr_min": integralMetrics['hr_min'],
                    "altitude_avg": integralMetrics['altitude_avg'],
                    "altitude_max": integralMetrics['altitude_max'],
                    "altitude_min": integralMetrics['altitude_min'],
                    "ascent": integralMetrics['ascent'],
                    "descent": integralMetrics['descent'],
                    "steps": integralMetrics['steps'],
                    "num_of_hills": numhills,
                    "avg_altitude": avg,
                    "avg_ascent": avgAscent,
                    "distance_hills": distance_hills,
                    "hills_share": hills_share
                }

                #print(single_result)
                #SaveResultArrayPickle(single_result)
        except:
            print("Error, file " + filename)


nekaj = {
    "activity_type": "novo",
    "id": 2,
    "dodatno": "nevem"
}
novo = {
    "activity_type": "druga aktivnost"
}
isto = {
    "activity_type": "druga aktivnost"
}

def task1():
    ReadFiles()
    #SortAndWriteCSV()

# task1()


