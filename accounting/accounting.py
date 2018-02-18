import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(5)


def which_year_max(table):
    profit_by_year = {}

    for line in range(len(table)):
        in_out = [0,0]

        if profit_by_year.get(table[line][3]) != None :
            if table[line][4] == "in":
                profit_by_year[table[line][3]][0] += int(table[line][5])
            elif table[line][4] == "out":
                profit_by_year[table[line][3]][1] += int(table[line][5])

        else:
            if table[line][4] == "in":
                in_out[0] += int(table[line][5])
            elif table[line][4] == "out":
                in_out[1] += int(table[line][5])
            profit_by_year[table[line][3]] = in_out
            
    for year in profit_by_year:
        profit_by_year[year] = profit_by_year[year][0] - profit_by_year[year][1]
    
    return int(max(profit_by_year, key=profit_by_year.get))

def avg_amount(table, year):
    profit_by_year = {}
    items_count = 0

    for line in range(len(table)):
        in_out = [0,0]

        if profit_by_year.get(table[line][3]) != None :
            if table[line][4] == "in":
                profit_by_year[table[line][3]][0] += int(table[line][5])
            elif table[line][4] == "out":
                profit_by_year[table[line][3]][1] += int(table[line][5])

        else:
            if table[line][4] == "in":
                in_out[0] += int(table[line][5])
            elif table[line][4] == "out":
                in_out[1] += int(table[line][5])
            profit_by_year[table[line][3]] = in_out
            
    for key in profit_by_year:
        profit_by_year[key] = profit_by_year[key][0] - profit_by_year[key][1]
    
    for line in range(len(table)):
        if int(table[line][3]) == year:
            items_count += 1

    current_profit = int(profit_by_year[str(year)])

    return current_profit/items_count
