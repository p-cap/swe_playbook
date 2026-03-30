nums = [1,2]
n = len(nums)
result = []
path = []
used = [False] * n # The "occupied" sign for the chairs

def backtrack():
    # BASE CASE: All seats are filled
    if len(path) == len(nums):
        result.append(path[:])
        return

    # THE LOOP: Look at every chair for the next slot
    for i in range(n):

        # PRUNING: Is this person already sitting down?
        if used[i]:
            continue
        
        # 1. SIT DOWN: Mark as used and add to path
        used[i] = True
        path.append(nums[i])

        # 2. RECURSE: Fill the next slots
        backtrack()

        # 3. STAND UP: Backtrack (The "Undo")
        path.pop()
        used[i] = False

backtrack()
print(result)