from typing import List

Vector = List[float]

height_weight_age = [70,170,40] #Inches,pounds,years

def subtract(v: Vector,w:Vector)-> Vector:
    '''Adds corresponding elements'''
    assert len(v) == len(w),'''Vectors must be the same lenght'''
    #v_i and w_i are variable created
    return [v_i - w_i for v_i, w_i in zip(v,w)]

#Assert is a test to certify the values are correct the subtraction of 5 and 4 = 1, 7 and 5 = 2,  9 and 6 = 3
#This statement is True, if you change 5 for another number that doesn't match 1 in the final vector it will raise an error/exception.
assert subtract([5,7,9],[4,5,6]) == [1,2,3]