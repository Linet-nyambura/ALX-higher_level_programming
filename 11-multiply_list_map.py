#function that returns a list with all values 
#multiplied by a number without using any loops
def multiply_list_map(my_list=[], number=0):
#x - represent each element in my_list
    return list(map(lambda x : x * number, my_list))
#calling the function
my_list = [1, 2, 3, 4, 5, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)