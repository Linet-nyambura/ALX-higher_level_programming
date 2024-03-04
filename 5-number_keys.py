#function that returns the number of keys in a dictionary
def number_keys(a_dictionary):
    return len(a_dictionary)
#calling a function
a_dictionary ={'langauge': 'C', 'number': 13, 'track': 'Low level'}
nb_keys = number_keys(a_dictionary)
print(nb_keys)