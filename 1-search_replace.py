#function that replaces all occurrences of an element by another in a new list
def search_replace(my_list, search, replace):
    #used to store the new list
    new_list = []

    for items in my_list: #iterates over the items in the list
        if items == search:
            return items
        new_list.append(replace)
    else:
        new_list.append(items)

    return new_list
#calling the function
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)