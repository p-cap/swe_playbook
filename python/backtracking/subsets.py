nums = [1,2]
result = []
subset = []

"""
- call backtrack(0)
- BASE CASE: if the current index, i, is greater than or equal to the length of nums, we add the shallow copy of subset and add it to result
- we add ith element in nums
- we append it to subset
- call backtrack(i + 1)
- pop from subset
- call backtrack(i + 1)
"""


def backtrack(i):
    if  i >= len(nums):
        result.append(subset[:])
        return
    
    subset.append(nums[i])
    backtrack(i + 1)

    subset.pop()
    backtrack(i + 1)

backtrack(0)
print(result)