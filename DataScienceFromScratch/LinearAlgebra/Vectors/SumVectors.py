from typing import List

Vector = List[float]

height_weight_age = [70,170,40] #Inches,pounds,years

def add(v: Vector,w:Vector)-> Vector:
    '''Adds corresponding elements'''
    assert len(v) == len(w),'''Vectors must be the same lenght'''
    #v_i and w_i are variable created
    return [v_i + w_i for v_i, w_i in zip(v,w)]

#Assert is a test to certify the values are correct the sum of 1 and 4 = 5, 2 and 5 = 7, 3 and 6 = 9
#This statement is True, if you change 1 for another number that doesn't match 5 in the final vector it will raise an error/exception.
assert add([1,2,3],[4,5,6]) == [5,7,9]
