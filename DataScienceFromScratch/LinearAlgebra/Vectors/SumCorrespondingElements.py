from typing import List

Vector = List[float]



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


#every first elements are being summed to result 16 and every second element are being summed to result 20,
#creating a new vector[16,20]
assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]


