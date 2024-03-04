#function that returns a set of common elements in two sets
def common_elements(set_1, set_2):
    common_set = set_1.intersection(set_2)
    return common_set
   # common_set = set()

#for elements in set_1:#iterates through each element in set_1
        
       #check if the elements are also in set_2
 #      if elements in set_2:
  #      common_set.add(elements)
   # return common_set        
#calling a function
set_1 = {'Python', ' C', 'Javascript'}
set_2 = {'Bash', 'C', 'Ruby', 'Perl'}
c_set = common_elements(set_1, set_2)
print(c_set)