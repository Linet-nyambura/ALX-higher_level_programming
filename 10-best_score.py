#function nthat returns a key with the biggest integer value
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_score = max(a_dictionary.values())#finds the maximum values in the dictionary
    for key, value in a_dictionary.items(): #iterates through dictionary items
         if value == max_score:
            return key
        
        #if no score found
         return None
    
#calliing a function
a_dictionary = {'John':12, 'Bob': 14, 'Mike' : 14, 'Molly' :16, 'Adam': 10}
best_key = best_score(a_dictionary)
print('Best Core: {}'.format(best_key))

best_key = best_score(None)
print('Best score: {}'.format(best_key))
    