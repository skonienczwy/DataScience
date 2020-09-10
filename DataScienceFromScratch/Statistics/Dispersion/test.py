from typing import List


Vector = List[float]

def dot( v:Vector, w:Vector) -> Vector:
    ''''Computes v_1 * w_1 + ... v_n * w_n'''
    assert  len(v) == len(w)##Vectors must be same length

    return  sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares( v:Vector) -> Vector:
    ''''Returns v_1 * V_1 + ... v_n * V_n'''
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14  # 1*1+2*2+3*3