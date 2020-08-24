from typing import List

Vector = List[float]

def scalar_multiply(c: float, v:Vector) -> Vector:
    ''''Multiplies  everey element by c'''
    return [c* v_i for v_i in v]


assert scalar_multiply(2,[1,2,3]) == [2,4,6]


def vector_sum(vectors:List[Vector])-> Vector:
    '''Sums all corresponding elements'''
   #Check that vector is not empty
    assert vectors, 'No Vecotors provided!'

    #Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors),'Different sizes!'

    #the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
def vector_mean(vectors: List[Vector]) -> Vector:
    '''Computes tje element-wise average'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))



assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]