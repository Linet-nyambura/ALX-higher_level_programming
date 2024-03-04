#function that prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary)
    for key in sort_keys:
        print(f"{key}: {a_dictionary[key]}")

#calling a function
my_dict = {"banana": 3, "apple": 2, "orange": 5} 
dictionary = print_sorted_dictionary(my_dict)
print(dictionary)
