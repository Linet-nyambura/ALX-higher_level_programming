#function that computess over the sqaures of a matrix
def square_matrix_simple(matrix=[]):
    #creates a new matrix to store the squared values
    result_matrix = []

    for row in matrix:#iterates over the original matrix
        #creates a new row to store the squared values for the current row
        squared_row = []
        #iterates over the elements in the row
        for num in row:
            squared_row.append(num ** 2)
            result_matrix.append(squared_row)
        return result_matrix
#calling a function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)
            

