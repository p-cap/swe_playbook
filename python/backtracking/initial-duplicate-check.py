"""
The initial check in looking at elements that are beside each other is the last and first element of the list. In the example below, once the list is sorted, the first and last element of the list is checked. 
"""
candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
print(candidates)

for i in range(len(candidates)):
    print(f"candidates[i]: {candidates[i]}")
    print(f"candidates[i]: {candidates[i - 1]}")
    break