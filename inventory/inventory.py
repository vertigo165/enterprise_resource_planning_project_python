import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(2)


def get_available_items(table):
    current_year = 2017
    available_items = []

    for line in table:
        if int(line[3]) + int(line[4]) >= current_year:
            line[3] = int(line[3])
            line[4] = int(line[4])
            available_items.append(line)
    
    return available_items


def get_average_durability_by_manufacturers(table):
    average = {}

    for line in table:
        temp = []

        if line[2] not in average:
            temp.append(int(line[4]))
            average[line[2]] = temp
        else:
            average[line[2]].append(int(line[4]))

    for item in average:
        sum_of_durability = 0

        for nums in average[item]:
            sum_of_durability += nums

        average[item] = round(sum_of_durability/len(average[item]), 2)
    
    return average