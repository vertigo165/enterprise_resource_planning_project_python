import data_manager

def print_table(table, title_list):
    table.insert(0,title_list)
    max_length_per_columns = []
    sum_lengths = 0

    for column in range (len(table[0])) :
        temp = 0
        for row in range (len(table)) :
            if len(str(table[row][column])) > temp :
                temp = len(str(table[row][column]))
        max_length_per_columns.append(temp)
    
    for i in range(len(max_length_per_columns)):
        sum_lengths += max_length_per_columns[i]

    print(" /", end='')

    for i in range(sum_lengths+len(table[0])*3-1):
        print("=",end='')

    print("\ ")

    for row_i in range(len(table)):
        row = table[row_i]
        for cell_j in range(len(row)):
            cell = row[cell_j]
            width = max_length_per_columns[cell_j]
            print(' | ' + cell.center(width), end='')
        print(' | ')

    print(" \\", end='')

    for i in range(sum_lengths+len(table[0])*3-1):
        print("=",end='')

    print("/ ")

    pass


def print_result(result, label):
    print(label)
    print(result)
    pass


def print_menu(title, list_options, exit_message):
    print(title + ":")
    for_count = 1

    for opts in list_options :
        print("\t(%s) " %for_count + opts)
        for_count += 1
    
    print("\t(0) " + exit_message)

    pass


def get_inputs(list_labels, title):
    print(title)
    inputs = []
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]))

    return inputs


def print_error_message(message):
    print(message)
    pass