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

num_friends = [1,10,2,9,5,2]
print(de_mean(num_friends))
print(variance(num_friends))

