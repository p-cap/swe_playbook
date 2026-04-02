# this implementation is similar to permutation
from turtle import back


result = []
nums = [1,2]

def backtrack(start, path):
    result.append(path[:])

    for i in range(start, len(nums)):
        
        # make a choice
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0,[])
print(result)