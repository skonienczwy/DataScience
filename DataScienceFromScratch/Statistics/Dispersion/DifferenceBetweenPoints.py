from typing import List


num_friends = [1,10,2,9,5,2]

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


data_range(num_friends)


print(data_range(num_friends))