#function that adds all unique integers in a list(only once for each integer)
def uniq_add(my_list=[]):
    unique_numbers = set(my_list) # converts the list to a set to remove duplicates
    return sum(unique_numbers) # returns the sum of unique numbers
#calling the function
my_list = [1, 2, 3, 1, 4, 2, 5]
uniquenumbers = uniq_add(my_list)
print(uniquenumbers)