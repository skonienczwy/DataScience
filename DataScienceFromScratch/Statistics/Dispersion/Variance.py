import sys
sys.path.append('DataScienceFromScratch\LinearAlgebra\Vectors')
from SumOfSquares import sum_of_squares
from typing import List
from statistics import mean



def de_mean(xs: List[float]) -> List[float]:
    '''Translate xs by subtracting its mean (so the result has mean 0)'''
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    '''Almost the average squared deviation from the mean'''    
    # assert len(xs) >= 2  #Variance requires at least two elements

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) /(n-1)

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# print(de_mean(num_friends))
# print(variance(num_friends))

