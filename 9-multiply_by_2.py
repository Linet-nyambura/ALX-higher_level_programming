# function that return a new dictionary with all values 
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
#calling the function
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(new_dict)
        