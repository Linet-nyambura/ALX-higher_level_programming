#function that reeturns the weighted average of all integers tuple
#<score>, <weight>
def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    sum_product = sum(score * weight for score, weight in my_list)#calculates the sum of products
    sum_weight = sum(weight for _, weight in my_list)#calculate the sum of weights

    return sum_product / sum_weight #return the weighted average

        