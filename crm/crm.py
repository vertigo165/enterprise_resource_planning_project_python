import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(4)


def get_longest_name_id(table):
    longest = [["",None]]

    for i in range(len(table)):
        if len(table[i][1]) > len(longest[0][0]):
            longest = [[table[i][1],table[i][0]]]
        elif len(table[i][1]) == len(longest[0][0]):
            longest.append([table[i][1],table[i][0]])

    lst = common.list_order(longest)
    
    return lst[0][1]


def get_subscribed_emails(table):
    subscribe = []

    for line in range(len(table)):
        temp_str = ""
        if table[line][3] == "1":
            temp_str = table[line][2]+";"+table[line][1]
            subscribe.append(temp_str)
    
    return subscribe


def get_name_by_id(id):
    table = data_manager.get_table_from_file("crm/customers.csv")
    all_customers = []

    if common.is_id_exists(table, id) == True:
        for line in table:
            if line[0] == id:
                return line[1]


def get_name_by_id_from_table(table, id):
    if common.is_id_exists(table, id) == True:
        for line in table:
            if line[0] == id:
                return line[1]


def get_all_customer_ids():
    table = data_manager.get_table_from_file("crm/customers.csv")
    all_customers = []

    for line in table:
        all_customers.append(line[1])
        
    return all_customers
