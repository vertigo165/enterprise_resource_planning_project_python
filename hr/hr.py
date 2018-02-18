import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(3)


def get_oldest_person(table):
    oldest_age = 9999
    oldest = []

    for i in range(len(table)):
        if oldest_age == int(table[i][2]):
            oldest.append(table[i][1])
            oldest_age = int(table[i][2])

        elif oldest_age < int(table[i][2]):
            oldest_age = int(table[i][2])
            oldest = []
            oldest.append(table[i][1])
    
    return oldest


def get_persons_closest_to_average(table):
    irr_age = 9999
    closest = []
    sum_of_ages = 0

    for i in range(len(table)):
        sum_of_ages += int(table[i][2])
    
    average_age = sum_of_ages/len(table)

    for i in range(len(table)):
        if abs(average_age-irr_age) == int(table[i][2])-irr_age:
            oldest.append(table[i][1])
            irr_age = int(table[i][2])
            
        elif abs(average_age-irr_age) < int(table[i][2])-irr_age:
            irr_age = int(table[i][2])
            closest = []
            closest.append(table[i][1])
    
    return closest