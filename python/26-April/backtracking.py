# I am looking for combinations not permutations
# combinations does not consider order
# permutations does


"""
def get_subsequences(arr, k):
    res = []
    
    def backtrack(start, path):
        # Base Case: found a subsequence of length k
        if len(path) == k:
            res.append(path[:])
            return
        
        # Recursive Step: Try all elements starting from 'start'
        for i in range(start, len(arr)):
            path.append(arr[i])      # Pick the element
            backtrack(i + 1, path)   # Move to next index
            path.pop()               # Backtrack (Don't pick)
            
    backtrack(0, [])
    return res

# Example: [1, 2, 3], k=2 -> [[1, 2], [1, 3], [2, 3]]

Combination: A subset of items where order is ignored ($[1, 2]$ is the same as $[2, 1]$).
Subsequence: A subset of items that must stay in their original relative order
"""

# let's do the backtrack problem

from unittest import result


res = []
k = 2
my_array = [1, 2, 3]

def backtrack(start, path):
    if len(path) == k:
        res.append(path[:])
        return
    for i in range(start, len(my_array)):
        path.append(my_array[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, [])
print(res)