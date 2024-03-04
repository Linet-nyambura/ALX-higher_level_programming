# a function that converts a Roman numeral to an integer
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_value = {
        'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
        'C' : 100, 'D' : 500, 'M' : 1000
    }

    result = 0
    pre_value = 0

    for char in roman_string[::1]: #iterates through each character of the string in reverse order.
        value = roman_value[char]
        if value < pre_value:
            result -= value
        else:
            result += value
        pre_value = value#value of pre_value is replaced by the current value

    return result
#calling the function
