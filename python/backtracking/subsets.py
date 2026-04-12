nums = [1,2]
result = []
current_path = []
n = len(nums)

def backtrack(start):
    result.append(current_path[:])
    for i in range(start, n):
        current_path.append(nums[i])
        # i added start not i
        # i should debug but not look at other code to reference
        backtrack(i + 1)
        current_path.pop()
        
backtrack(0)
print(result)