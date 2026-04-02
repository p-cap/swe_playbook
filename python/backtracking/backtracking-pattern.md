## Backtracking General Pattern
- Base Case
- Choices
- Constraints
- Backtracking steps

### Base Case
- The subset problem DOES NOT have a base case
- For the permutation problem, we check if the length of the list is equal to the input list
- For combination sum, the target is the constraint

# Backtracking Strategy & Patterns

## 🎤 Technical Interview Strategy
When an interviewer asks for "all possible" configurations, emphasize these four pillars:

1.  **The State Space Tree:** Explain that you are exploring a decision tree where each node represents a partial solution.
2.  **The Choice:** Define what you are adding at each step (e.g., "I am choosing the next character for the partition").
3.  **The Constraints (Pruning):** Mention that you will stop exploring a branch as soon as it violates a rule (e.g., "If the current string isn't a palindrome, I won't recurse further").
4.  **The Cleanup:** Explicitly mention the **Backtrack step** (`path.pop()`), which resets the state so the next iteration of the loop can start with a "clean slate."

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