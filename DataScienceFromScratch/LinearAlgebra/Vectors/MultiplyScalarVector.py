from typing import List

Vector = List[float]

def scalar_multiply(c: float, v:Vector) -> Vector:
    ''''Multiplies  everey element by c'''
    return [c* v_i for v_i in v]


assert scalar_multiply(2,[1,2,3]) == [2,4,6]