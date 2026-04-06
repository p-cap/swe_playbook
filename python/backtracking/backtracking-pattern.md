## Backtracking General Pattern
- Base Case
- Choices
- Constraints
- Backtracking steps

## ISSUES
- remember, you need a SHALLOW COPY OF THE LIST
- 



### Base Case
- The subset problem DOES NOT have a base case
- For the permutation problem, we check if the length of the list is equal to the input list
- For combination sum, the target is the constraint

### Combination in motion
- the backtrack is called by passing in an index
- the parent backtrack holds the first element of list
- i + 1 ensures we have a different start on every for loop
- this also inheritly prevents the same numbers being added within the same list
- this also is great for combinations because order does not matter meaning [1,2] and [2,1] are the same

# Backtracking Strategy & Patterns

---

## 🚀 Master Logic Table (Quick Reference)

| Strategy | Trigger Words | Selection Logic (The "Why") | Key LeetCode |
| :--- | :--- | :--- | :--- |
| **Subsets** | "All possible," "Power set," "Combinations" | **`i + 1`**: Always move forward to avoid reusing the same element or creating duplicate sets. | 78, 90 |
| **Permutations** | "Arrangements," "Order matters," "All sequences" | **`used` set**: Allow any element from the input, as long as it isn't already in the current path. | 46, 47 |
| **Combinations** | "Groups of size K," "Pick K," "Team of" | **Base Case `len == k`**: Similar to Subsets, but you only "save" the path when it reaches the target depth. | 77, 39, 40 |
| **Partitioning** | "Split string," "Cut into," "Decompose" | **Loop as End Index**: The `for` loop index `i` acts as the "cutting point" for the current segment. | 131, 93 |
| **Constraint / Pruning** | "Valid," "Rules," "N-Queens," "Sudoku" | **Pre-check**: Check `is_valid()` *before* recursing to "kill" bad branches early. | 51, 37, 79 |

---

## 💡 Visual Logic Comparison

| Feature | Subsets / Combinations | Permutations |
| :--- | :--- | :--- |
| **Does Order Matter?** | No (`[1,2]` == `[2,1]`) | Yes (`[1,2]` != `[2,1]`) |
| **Loop Starting Point** | `for i in range(start, len(nums))` | `for i in range(len(nums))` |
| **Recursion Step** | `backtrack(i + 1, path)` | `backtrack(path)` |
| **Duplicate Handling** | Sort + `if i > start and nums[i] == nums[i-1]` | Sort + `if used[i]` or `if i > 0 and nums[i] == nums[i-1] and not used[i-1]` |

---

## ⚠️ Common Interview "Gotchas"

> 💡 **The Reference Trap:** > In Python, lists are passed by reference. If you do `res.append(path)`, you will end up with a list of empty lists. Always use **`res.append(path[:])`** to save a snapshot of the current state.

> 🚀 **The Start Index:** > In Subsets/Combinations, passing `i + 1` (the loop index) to the next call is what prevents you from using the same element twice. Using `start + 1` by mistake is a common bug that leads to duplicate combinations.

--

## CODE

### Subset
> This code and permutation will be similar so it is easier to remember. Everytime the recursive function is called, we add the current state of path. 

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result
```
ISSUES:
- FORGOT SHALLOW COPY: `result.append(path[:])`
- remember to pass a index on every backtrack call
- inside every for loop, pass the CURRENT INDEX PLUS 1 (i + 1) which prevents using the same element twice
- twice meaning same elements within the same list

### Permutation
> For permutation, we also utilize a for loop however, each recursive function's for loop start with zero. It's important to check if the current nums is in the path and if so, we continue with the next iteration. 

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack()
                path.pop()
            
        backtrack()
        return result
```
- ISSUES
- was not clear on the suttle differences between subset and permutation
- FORGOT THE RETURN WHEN HITTING THE BASE CASE
```python
if len(path) == len(nums):
    result.append(path[:])
    return
```
- checking if the nums[i] is in path to prevent duplicates
```python
for i in range(len(nums)):
    if nums[i] in path:
        continue
```

### Combination
> the combination is almost the same with subsets with a slight difference. It checks if the k is equal to the length of the path list 

```python 
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return 
            
            # dynamic start in the loop
            # this is the same with subset
            for i in range(start,n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        
        # start with 1
        backtrack(1)
        return result
```
ISSUES: 
- subset is very combination
- the only different is the base case checks for the length for each list 