"""
nums = [3, 1, 3, 2, 1, 1]
nums.sort()

# comparing the duplicates withouth skipping the first element is still right
for i in range(len(nums)):
    if nums[i] == nums[i-1]:
        print("dupes")
        continue
"""


nums = [1,2,2]
output = [[],[1],[1,2],[1,2,2],[2],[2,2]]
result = []

def backtrack(start, path):
    result.append(path[:])
    for i in range(start, len(nums)):
        # i > start ensures once i is not the beginning of the loop, it can start comparing
        # this is more of an optimization or 
        if i > start and nums[i-1] == nums[i]:
            continue
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
backtrack(0,[])
print(result)