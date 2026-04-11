## BACKTRACKING GENERAL PATTERN
- Base Case
- Choices
- Constraints
- Backtracking steps

## RESOURCES TO REMEMBER
- Cracking the coding interview book
- Google Drive resources from Logan

## ISSUES TRACKING / COMMON GOTCHAS
- remember, you need a SHALLOW COPY OF THE LIST
- for subsets, I still need some clarification on how the code is:
    - preventing duplicate subsets
    - preventing duplicates within inputs with different elements
- Combination Sum, passing only `i` through the parameter vs `i+1` and also accounting current sum and the current element

## Pattern Validation through problems
### Subset
- FILE_PATH: python/backtracking/subsets.py
- Base Case: Subset DOES NOT have a base case
- Choices: The choices are based on the addition of elements from `current_path` variable?
- Constraints: No constraints for this problem
- Backtracking steps
    - for loop
    - add current element to build the subset
    - call the backtracking function with `i+1` on every backtracking call
    - pop form the `current_path` list 

### Permutation
- FILE_PATH: python/backtracking/permutations.py
- Base Case: If `current_path` length is equal to the input length, add the `current_path` to the `result`
- Choices: We add elements but we make sure we do not have duplicate elements by checking the `current_path`
- Constraints: ?????
- Backtracking steps:
    - for loop
    - add current element to `current_path` 
    - call the backtracking function without a parameter

### Combination in motion
- FILE_PATH: python/backtracking/combination.py
- Base Case: If `current_path` length is equal to `k`, add `current_path` to `result`
- Choices: We add the element based on the incremental starting of the for loop on every backtracking call
- Constraints: The starting index is based on `i+1` from the backtrack parameter
- Backtracking steps:
    - `i+1` is the starting index of the for loop
    - for loop
    - add element to `current_path`
    - call backtrack function
    - pop element 

### Combination Sum
- FILE PATH: python/backtracking/combination-sum.py
- BASE CASE:
    - the running total equal to the target, we append elements onto the result
    - if the total greater than the target, return
- CHOICES: 
    - We can choose unlimited elements of the same element to get to the sum
    - the list can be in any order
- CONSTRAINTS:
    - ?????
- BACKTRACKING STEPS:
    - if the `total` equal to the `target`, added the list to the result
    - if the `total` is greater than the target, return
    - append elements onto a `path` list
    - backtrack function has two parameters, the i for the index and the running total
    - NOTE: Make when passing the total, we are adding total to the current element

## REFERENCE
---

### 🚀 Master Logic Table (Quick Reference)

| Strategy | Trigger Words | Selection Logic (The "Why") | Key LeetCode |
| :--- | :--- | :--- | :--- |
| **Subsets** | "All possible," "Power set," "Combinations" | **`i + 1`**: Always move forward to avoid reusing the same element or creating duplicate sets. | 78, 90 |
| **Permutations** | "Arrangements," "Order matters," "All sequences" | **`used` set**: Allow any element from the input, as long as it isn't already in the current path. | 46, 47 |
| **Combinations** | "Groups of size K," "Pick K," "Team of" | **Base Case `len == k`**: Similar to Subsets, but you only "save" the path when it reaches the target depth. | 77, 39, 40 |
| **Partitioning** | "Split string," "Cut into," "Decompose" | **Loop as End Index**: The `for` loop index `i` acts as the "cutting point" for the current segment. | 131, 93 |
| **Constraint / Pruning** | "Valid," "Rules," "N-Queens," "Sudoku" | **Pre-check**: Check `is_valid()` *before* recursing to "kill" bad branches early. | 51, 37, 79 |

---

### 💡 Visual Logic Comparison

| Feature | Subsets / Combinations | Permutations |
| :--- | :--- | :--- |
| **Does Order Matter?** | No (`[1,2]` == `[2,1]`) | Yes (`[1,2]` != `[2,1]`) |
| **Loop Starting Point** | `for i in range(start, len(nums))` | `for i in range(len(nums))` |
| **Recursion Step** | `backtrack(i + 1, path)` | `backtrack(path)` |
| **Duplicate Handling** | Sort + `if i > start and nums[i] == nums[i-1]` | Sort + `if used[i]` or `if i > 0 and nums[i] == nums[i-1] and not used[i-1]` |

---

