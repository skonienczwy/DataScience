from typing import List,Callable


Matrix = List[List[float]]




def make_matrix(num_rows: int, 
                num_cols: int, 
                entry_fn: Callable[[int,int],float]) -> Matrix:
    '''Return a num_rows x num_cols matrix
       whose (i,j)-th entry is entry_fn(i,j
    '''
    #given i , create a list [entry_fn(i,0),...]  create one list for each i  
    return [[entry_fn(i , j) for j in range(num_cols)] for i in range(num_rows)]       
                             
def identity_matrix (n: int) -> Matrix:
    '''Returns the nxn identify matrix '''
    return make_matrix(n,n,lambda i ,j: 1 if i==j else 0)



print(identity_matrix(5))    