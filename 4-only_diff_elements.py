#function that returns a set of all elements present in only a set
def only_diff_elements(set_1, set_2):
    diff_set = (set_1 - set_2) | (set_2 - set_1)
    #diff_set = set_1.symmetric_difference(set_2)
    return diff_set
#calling a function
set_1 = {'python', 'C', 'Javasript'}
set_2 = {'Bash', 'C', 'Ruby', 'Perl'}
od_set = only_diff_elements(set_1, set_2)
print(od_set)