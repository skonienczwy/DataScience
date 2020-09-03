import  math
from typing import List


Vector = List[float]


def dot( v:Vector, w:Vector) -> Vector:
    ''''Computes v_1 * w_1 + ... v_n * w_n'''
    assert  len(v) == len(w)##Vectors must be same length

    return  sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares( v:Vector) -> Vector:
    ''''Returns v_1 * V_1 + ... v_n * V_n'''
    return dot(v,v)

def subtract(v: Vector,w:Vector)-> Vector:
    '''Adds corresponding elements'''
    assert len(v) == len(w),'''Vectors must be the same lenght'''
    #v_i and w_i are variable created
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def squared_distance(v:Vector,w:Vector)-> float:
    '''Computes (v_1 - W_1) **2 + ... (v_n - w_n)**2'''
    return sum_of_squares(subtract(v,w))

def distance(v:Vector,w:Vector)->float:
    '''Computes the distance between v and w'''
    return math.sqrt(squared_distance(v,w))



print(squared_distance([1,2],[2,1]))

##or

# def magnitude(v: Vector) -> float:
#     '''Returns the magnitude (or length) of v'''
#     return math.sqrt((sum_of_squares(v)))  #math.sqrt is square root function
#
# def distance(v:Vector,w:Vector)->float:
#     '''Comoutes the distance between v and w'''
#     return magnitude(subtract(v,w))


