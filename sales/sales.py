import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(0)


def get_lowest_price_item_id(table):
    lowest_price_id = []
    lowest_price = int(table[0][2])

    for i in range(len(table)):
        if int(table[i][2]) < lowest_price:
            lowest_price = int(table[i][2])
    
    for i in range(len(table)):
        if int(table[i][2]) == lowest_price:
            lowest_price_id.append(table[i][0])

    lowest_price_id = list(reversed(common.list_order(lowest_price_id)))

    return lowest_price_id[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    new_table = []

    for line in table:
        curr_year = int(line[5])
        curr_month = int(line[3])
        curr_day = int(line[4])

        if curr_year >= year_from and curr_year <= year_to:
            if curr_month >= month_from and curr_month <= month_to:
                if curr_day >= day_from and curr_day < day_to:
                    new_table.append(line)

    return new_table


def get_title_by_id(id):

    table = data_manager.get_table_from_file("sales/sales.csv")
    if common.is_id_exists(id) == True:
        for line in table:
            if line[0] == id:
                return line[1]


def get_title_by_id_from_table(table, id):
    if common.is_id_exists(id) == True:
        for line in table:
            if line[0] == id:
                return line[1]


def get_item_id_sold_last():
    last_sold_id = ""
    table = data_manager.get_table_from_file("sales/sales.csv")
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[0])
            return last_sold_id


def get_item_id_sold_last_from_table(table):
    last_sold_id = ""
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[0])
            return last_sold_id


def get_item_title_sold_last_from_table(table):
    last_sold_id = ""
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[1])
            return last_sold_id


def get_the_sum_of_prices(item_ids):
    table = data_manager.get_table_from_file("sales/sales.csv")
    sum_of_prices = 0

    for ids in item_ids:
        for line in table:
            if ids == line[0]:
                sum_of_prices += int(line[2])
    
    return sum_of_prices


def get_the_sum_of_prices_from_table(table, item_ids):
    sum_of_prices = 0

    for ids in item_ids:
        for line in table:
            if ids == line[0]:
                sum_of_prices += int(line[2])
    
    return sum_of_prices


def get_customer_id_by_sale_id(sale_id):
    table = data_manager.get_table_from_file("sales/sales.csv")

    for line in table:
        if sale_id == line[0]:
            return str(line[6])


def get_customer_id_by_sale_id_from_table(table, sale_id):
    for line in table:
        if sale_id == line[0]:
            return str(line[6])


def get_all_customer_ids():
    table = data_manager.get_table_from_file("sales/sales.csv")
    customer_ids = set()

    for line in table:
        if line[6] not in customer_ids:
            customer_ids.add(line[6])
    
    return customer_ids


def get_all_customer_ids_from_table(table):
    customer_ids = set()

    for line in table:
        if line[6] not in customer_ids:
            customer_ids.add(line[6])
    
    return customer_ids


def get_all_sales_ids_for_customer_ids():
    table = data_manager.get_table_from_file("sales/sales.csv")
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_ids_for_customer_ids = {}

    for ids in all_customer_ids:
        temp = []
        for line in table:
            if ids == line[6]:
                temp.append(line[0])
        sales_ids_for_customer_ids[ids] = temp

    return sales_ids_for_customer_ids


def get_all_sales_ids_for_customer_ids_form_table(table):    
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_ids_for_customer_ids = {}

    for ids in all_customer_ids:
        temp = []
        for line in table:
            if ids == line[6]:
                temp.append(line[0])
        sales_ids_for_customer_ids[ids] = temp

    return sales_ids_for_customer_ids


def get_num_of_sales_per_customer_ids():
    table = data_manager.get_table_from_file("sales/sales.csv")
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_per_customers = {}

    for ids in all_customer_ids:
        sales_counter = 0
        for line in table:
            if ids == line[6]:
                sales_counter += 1
        sales_per_customers[ids] = sales_counter
    
    return sales_per_customers


def get_num_of_sales_per_customer_ids_from_table(table):
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_per_customers = {}

    for ids in all_customer_ids:
        sales_counter = 0
        for line in table:
            if ids == line[6]:
                sales_counter += 1
        sales_per_customers[ids] = sales_counter

    return sales_per_customers
