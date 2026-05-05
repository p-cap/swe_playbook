# %% [markdown]
# ### Combination Sum II
# This problem asks to return a list of elements that sum to a given target. It requires that our elements within each combination are unique. In other words, we cannot repeat the elements within the collected list of elements. We need to return the combination. 
# 
# ### Solution
# The combination sum II problem will utilize backtracking. We initialize the result list to store the list of combinations that makeup the sum. The backtrack function will take 3 paramters. First, it will take the list that will track elements that is iterate through the list. Second, we will have the remamining parameter. The third parameter will take current index of the for loop incremented by 1. Within the backtracking function, we will have two base cases. The first base case, we will check if our remaining paramter is equal to zero. When calling the backtrack function, we will decrement the remaining paramter by the current candidate of the loop. The second base will check if the remaining is less than or greater than the remaining. This will ensure our backtracking function will not be called as much. Then, we iterate through the for loop. Inside the for loop, we will add the elements, call the backtracking function and pop from the elements in the list. Adding and removing elements from the list allows us to include and exclude elements. Before calling the backtracking function, we'll need to sort the list. The reason why we need to sort the list so we can check for duplicates in the list. We check the duplicates inside the for loop? The answer is yes. In the sorted list, the first and last element is checked and if the elements are the same, we move to the iteration of the for loop

# %%
candidates = [10,1,2,7,6,1,5] 
target = 8

result = []

# sort the candidates
candidates.sort()

def backtrack(combinations, remaining, start):
    if remaining == 0:
        return
    if remaining < 0:
        return
    for i in range(start, len(candidates)):
        # we check for duplicate elements here
        # I guess we want to consider if i > start
        # this constraint allows the for loop to iterate one time and then start check duplicates
        if i > start and (candidates[i] == candidates[i - 1]):
            continue
        combinations.append(candidates[i])
        backtrack(combinations, remaining - candidates[i], i + 1)
        combinations.pop()
backtrack([], target, 0)
print(result)

# %% [markdown]
# ### Takeaways
# The combination sum II compared to the other combinations have the following differences. In combination sum I, we are passing the `i` as it is at every recursive call but with combination sum II, we are adding the `i` with 1 because we do not want duplicates that exists within the same combination. Speaking of duplicates, we also are checking for duplicates in the input list. To effectively check for duplicates, we'll need to sort the list. 

# %% [markdown]
# # Comparison of Combination, Combination Sum, and Combination Sum II
# 
# | **Aspect** | **Combination** | **Combination Sum** | **Combination Sum II** |
# |---|---|---|---|
# | **Problem Statement** | Find all combinations of k numbers from 1 to n | Find all unique combinations where numbers sum to target | Find all unique combinations where numbers sum to target |
# | **Input Constraints** | n (upper bound), k (size of combination) | Array of distinct integers, target sum | Array (may have duplicates), target sum |
# | **Element Reuse** | Each number used **at most once** | Each number can be used **unlimited times** | Each number used **at most once** |
# | **Array Property** | Implicit (1 to n) | All elements **distinct** | May contain **duplicates** |
# | **Sorting Required** | Not needed (1 to n is sorted) | Not required | **Required** (to group and skip duplicates) |
# | **Start Parameter** | Pass `i + 1` | Pass `i` (same index) | Pass `i + 1` (next index) |
# | **Duplicate Handling** | Natural (no duplicates in 1 to n) | Not needed (all distinct) | Must skip duplicates with `if i > start and arr[i] == arr[i-1]: continue` |
# | **Example Input** | n=4, k=2 | candidates=[2,3,6,7], target=7 | candidates=[10,1,2,7,6,1,5], target=8 |
# | **Example Output** | [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]] | [[2,2,3], [7]] | [[1,1,6], [1,2,5], [1,7], [2,6]] |
# | **Time Complexity** | O(C(n,k) · k) = O(n!/(k!(n-k)!)) | O(N^(T/M)) where T=target, M=min value | O(N · 2^N) subset exploration |
# | **Space Complexity** | O(k) recursion depth | O(T/M) recursion depth | O(N) recursion depth |
# | **LeetCode Problem** | #77 | #39 | #40 |∏


