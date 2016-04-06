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
        line = line.strip()
        line_item_list = line.split(",")

        # ensure value types are correct
        line_item_list[0] = str(line_item_list[0])
        line_item_list[1] = str(line_item_list[1])
        line_item_list[2] = float(line_item_list[2])
        line_item_list[3] = str(line_item_list[3])

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
    get user_input (to lowercase)
    while not user_input == "q"
        if user_input == "l"
            display items on file
            count = 0
            for each item in items_list
                display count + " - " + item[0] + " (" + item[1] + ") = $ " + item[2]
        else if user_input == "h"
            count = 0
            for each item in items_list
                if item[3] == in
                    display count + " - " + item[0] + " (" + item[1] + ") = $ " + item[2]
            display enter item number
            get item_choice
            items_list[item_choice] = [items_list[item_choice][0],items_list[item_choice][1],items_list[item_choice][2],"out"]
            display items_list[item_choice][0] + "hired for $" + items_list[item_choice][2]
        else if user_input == "r"
            (return an item)
        else if user_input == "a"
            (add new item to stock)

        display menu
        get user_input (to lowercase)

    (save to csv)
    display amount of items saved message
    display goodbye message

"""
def main():
    print("Items for hire - By Heylon White")
    items_list = load_items(ITEMS_FILE_NAME)
    print("{} items loaded from {}".format(len(items_list),ITEMS_FILE_NAME))

    print(MENU)
    user_input = input(">>> ").lower()

    while user_input != "q":
        if user_input == "l":
            print("All items on file (* indicates item is currently out):")
            count = 0

            for item in items_list:
                if item[3] == "out":
                    hire_status = "*"
                else:
                    hire_status = ""

                item_description = "{} ({})".format(item[0], item[1])
                print("{} - {:39} = ${:7.2f} {}".format(count, item_description, item[2], hire_status))
                count += 1
        print(MENU)
        user_input = input(">>> ").lower()
main()

# rgewegre


