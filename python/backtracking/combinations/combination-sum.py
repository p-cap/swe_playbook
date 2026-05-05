candidates = [2,3,5]
target = 8
result = []
path = []
n = len(candidates)

def backtrack(start, total):
    # BASE CASE: total and target are the same append to result
    if total == target:
        result.append(path[:])
        return 
    
    # BASE CASE 2: If total greater than taregt, return
    if total > target:
        return
    
    for i in range(start, n):
        path.append(candidates[i])
        # just pass in the i only so we can use duplicate entries and account for the running total
        backtrack(i,total + candidates[i])
        path.pop()        

backtrack(0,0)
print(result)