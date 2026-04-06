result = []
nums = [1,2]
path = []


def backtrack(start):
    result.append(path[:])

    for i in range(start, len(nums)):
        
        # make a choice
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

backtrack(0)
print(result)