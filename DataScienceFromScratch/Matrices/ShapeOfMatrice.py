from typing import Tuple,List


Matrix = List[List[float]]


A = [[1,2,3],  #A has 2 rows and 3 columns
     [4,5,6]]




def shape(A : Matrix ) -> Tuple[int,int]:
    '''Returns (# of rows of A, # of columns of A)'''     
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row

    return num_rows, num_cols
    

assert(shape([[1,2,3],[4,5,6]]) == (2,3)) # 2 rows and 3 columns