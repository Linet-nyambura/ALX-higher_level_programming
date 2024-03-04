#function that replaces or adds key/value in a dictionary
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
#calling a function
a_dictionary = {'language': 'C', 'number': 89, 'track': 'Low level'}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print(new_dict)
