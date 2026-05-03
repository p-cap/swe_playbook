candidates = [10,1,2,7,6,1,5] 
target = 8

result = []

# sort the candidates
candidates.sort()
print(candidates)
def backtrack(combinations, remaining, start):
    if remaining == 0:
        print("test")
        result.append(combinations[:])
        return
    if remaining < 0:
        print("remaining less than zero")
        return
    for i in range(start, len(candidates)):
        # we check for duplicate elements here
        # I guess we want to consider if i > start
        # this constraint allows the for loop to iterate one time and then start check duplicates
        if (i > start) and (candidates[i] == candidates[i - 1]):
            continue
        combinations.append(candidates[i])        
        backtrack(combinations, remaining - candidates[i], i + 1)
        combinations.pop()
backtrack([], target, 0)
print(result)