import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(1)


def get_counts_by_manufacturers(table):
    result = {}

    for line in table:
        if line[2] not in result:
            result[line[2]] = 1
        else:
            result[line[2]] += 1

    return result


def get_average_by_manufacturer(table, manufacturer):
    sum_of_instock = 0
    counter = 0

    for line in table:
        if manufacturer == line[2]:
            counter += 1
            sum_of_instock += int(line[4])
    
    return round((sum_of_instock/counter), 2)
