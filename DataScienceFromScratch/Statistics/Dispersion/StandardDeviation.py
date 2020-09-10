import math
from typing import List

from Variance import variance

num_friends = [1,10,2,9,5,2]

def standard_deviation(xs : List[float])-> float:
    '''The standard deviation  is the square root of the variance'''
    return math.sqrt(variance(xs))

print(standard_deviation(num_friends) )