from typing import List,Counter

num_friends = [1,10,2,9,5,2]

def mean(xs : List[float]) -> float:
    return sum(xs) / len(xs)


'''The underscores indicate tha therese are private functions, as they are 
intended to be called by ou median function but not by other people using 
our statistics library '''

def _median_odd(xs : List[float]) -> float:
    '''If len(xs)' is odd, the median is the middle element'''
    return sorted(xs) [len(xs) // 2]
    
def _median_even(xs : List[float]) ->float:
    '''If len(xs) is even, it is the average of the middle two elements'''
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2 
    return (sorted_xs[hi_midpoint -1 ] + sorted_xs[hi_midpoint])/2



def median(v: List[float])->float:
    '''Finds the middle-most value of v'''
    return _median_even(v)  if len(v) % 2 == 0 else _median_odd(v)



def quantile(xs: List[float], p: float)->float:
    '''Returns the pth-percentile valie in x'''
    p_index = int(p*len(xs))
    return sorted(xs)[p_index]

def mode(x: List[float]) -> float:
    '''Returns a list , since there might be more than one mode'''    
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i , count in counts.items() if count == max_count]




'''TESTS
x = mean(num_friends)  
y = median(num_friends)  
z = quantile(num_friends, 0.10)
m = mode(set(mode(num_friends)))
# # assert median([1,10,2,9,5]) == 5  
# # assert median([1,9,2,10]) == (2+9) /2 
# assert(quantile(num_friends, 0.25)) == 3
# assert(quantile(num_friends, 0.75)) == 9
# assert(quantile(num_friends, 0.90)) == 13

print(f' Mean: {x: .2f}')
print(f' Median: {y}')
print(f' Quantile: {z}')
print(f' Mode: {m}')

'''