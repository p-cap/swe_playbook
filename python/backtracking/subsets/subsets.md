Feature,Subsets I,Subsets II
Input Type,"Unique elements (e.g., [1, 2, 3])","Contains duplicates (e.g., [1, 2, 2])"
Pre-processing,None needed,Must sort() the array
Duplicate Check,None,if i > start and nums[i] == nums[i-1]: continue
Branching Logic,Explores every index once,"Prunes ""horizontal"" branches of the same value"
Result Set,All possible combinations,Only unique combinations
Time Complexity,O(N⋅2N),O(N⋅2N) (Pruning makes it faster in practice)