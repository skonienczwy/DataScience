from typing import Tuple,List


Matrix = List[List[float]]
Vector = List[float]

A = [[1,2,3],  #A has 2 rows and 3 columns
     [4,5,6]]





def get_row(A: Matrix, i: int) -> Vector:
    '''Returns the i-th row of A  (as a Vector)'''
    return print(A[i])  # A[i] is already the i-th row

def get_column(A: Matrix, j: int) -> Vector:
    '''Returns the j-th row of A  (as a Vector)'''

    return print([A_i[j] for A_i in A]) #jth element of A_i for each row A_i


get_row(A,0)
get_column(A,0)    