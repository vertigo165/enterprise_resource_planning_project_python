import os
import ui
import common
from sales import sales
from crm import crm


def start_module():
    
    common.submenu_of_managements(6)


def get_the_last_buyer_name():
    last_sold_item = sales.get_item_id_sold_last()
    last_buyer_id = sales.get_customer_id_by_sale_id(last_sold_item)
    last_buyer_name = crm.get_name_by_id(last_buyer_id)
    return last_buyer_name


def get_the_last_buyer_id():
    last_sold_item = sales.get_item_id_sold_last()
    last_buyer_id = sales.get_customer_id_by_sale_id(last_sold_item)
    return last_buyer_id


def get_the_buyer_name_spent_most_and_the_money_spent(table):
    result = []
    result.append(crm.get_name_by_id(get_the_buyer_id_spent_most_and_the_money_spent(table)[0]))
    result.append(get_the_buyer_id_spent_most_and_the_money_spent(table)[1])
    return tuple(result)


def get_the_buyer_id_spent_most_and_the_money_spent(table):
    all_customer_ids = list(sales.get_all_customer_ids_from_table(table))
    customers_spent = []
    highest_paid = 0
    customer_id = ""
    result =[]

    for ids in all_customer_ids:
        temp = 0
        temp_list = []
        for line in table:
            if ids == line[6]:
                temp += int(line[2])
        temp_list.append(ids)
        temp_list.append(temp)
        customers_spent.append(temp_list)
    
    for line in customers_spent:
        if line[1] > highest_paid:
            highest_paid = line[1]
            customer_id = line[0]

    result.append(customer_id)
    result.append(highest_paid)

    return tuple(result)


def get_the_most_frequent_buyers_names(num=1):
    temp = sales.get_num_of_sales_per_customer_ids()
    temp = sorted(temp.items(), key=lambda item:item[1], reverse=True)
    result = []

    for i in range(len(temp)):
        name_and_id = (crm.get_name_by_id(temp[i][0]), temp[i][1])
        result.append(name_and_id)

    return result[:num]


def get_the_most_frequent_buyers_ids(num=1):
    result = sales.get_num_of_sales_per_customer_ids()
    result = sorted(result.items(), key=lambda item:item[1], reverse=True)
    return result[:num]


def all_the_customers_who_did_not_buy_anything():
    crm_customers_list = crm.get_all_customer_ids()
    sales_customers_list = list(sales.get_all_customer_ids())
    result = []

    for customer in crm_customers_list:
        if customer not in sales_customers_list:
            result.append(customer)
    
    return result
