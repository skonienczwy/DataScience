import sys
sys.path.append('DataScienceFromScratch\LinearAlgebra\Statistics\CentralTendencies')
from CentralTendencies import quantile
from typing import List

num_friends = [1,10,2,9,5,2]

def interquartile_range(xs: List[float])->float:
    '''Returns the difference between the 75%-ile and the 25%-ile'''
    return quantile(xs,0.75) - quantile(xs, 0.25)

print(interquartile_range(num_friends))