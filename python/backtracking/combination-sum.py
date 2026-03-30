candidates = [2,2,4]
target = 4
result = []
path = []

def backtrack(i, total):
    if total == target:
        result.append(path[:])
        # not having a return made a difference because there were duplicates entries in result
        return 

    if i >= len(candidates) or total > target:
        return

    # appends the potential elements within candidates    
    path.append(candidates[i])

    # adding element with the same index
    backtrack(i, total + candidates[i])

    path.pop()
    # adding element with a different index
    backtrack(i + 1, total)
    
backtrack(0,0)
print(result)