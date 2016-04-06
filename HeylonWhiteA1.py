"""
CP1404 Assignment 1 - 2016
Items for hire
Heylon White
https://github.com/HeylonNHP/Assignment_1
21/03/16
"""

ITEMS_FILE_NAME = "items.csv"
MENU = "Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

"""
Pseudocode function load_items:

function load_itemsfilename)
    file_lines_list = []
    open filename as file_in for reading
    for each line in filename.readlines()
        strip white spaces and new line chars from line
        line_item_list = split line by ","
        append line_item_list converted to tuple to file_lines_list
    close file_in
    return file_lines_list
"""
def load_items(filename):
    file_lines_list = []
    file_in = open(filename, "r")
    for line in file_in.readlines():
        line.strip()
        line_item_list = line.split(",")
        file_lines_list.append(tuple(line_item_list))
    file_in.close()
    return file_lines_list


"""
Pseudocode function main:

function main()
    display welcome message

    items_list = load_items(FILENAME)
    display length of items_list + "items loaded from items.csv"

    display menu
    get user_input
    while not user_input (to lowercase) == "q"
        if user_input (to lowercase) == "l"
            display items on file
            count = 0
            for each item in items_list
                display count + " - " + item[0] + " (" + item[1] + ") = $ " + item[2]
        else if user_input (to lowercase) == "h"
            count = 0
            for each item in items_list
                if item[3] == in
                    display count + " - " + item[0] + " (" + item[1] + ") = $ " + item[2]
            display enter item number
            get item_choice
            items_list[item_choice] = [items_list[item_choice][0],items_list[item_choice][1],items_list[item_choice][2],"out"]
            display items_list[item_choice][0] + "hired for $" + items_list[item_choice][2]
        else if user_input (to lowercase) == "r"
            (return an item)
        else if user_input (to lowercase) == "a"
            (add new item to stock)

        display menu
        get user_input

    (save to csv)
    display amount of items saved message
    display goodbye message

"""
def main():
    print("Items for hire - By Heylon White")
    items_list = load_items(ITEMS_FILE_NAME)
    print("{} items loaded from {}".format(len(items_list),ITEMS_FILE_NAME))

    print(MENU)


main()

#rgewegre


