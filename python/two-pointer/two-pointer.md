## Two Pointer patterns
### FIXED WINDOW

#### 643. Maximum Average Subarray I
```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # currnet sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # I can iterate with a fixed window starting with 'k'?
        # this is another to iterate with a fixed window
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
```
- `for i in range(k, len(nums)):` -> we can start with k when iterating through the window
- `window_sum = window_sum - nums[i-k] + nums[i]`  
    - `- nums[i-k]` accounts for the element leaving the window
    - `+ nums[i]` element being added to the current window
#### 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
```python
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        """
        - k is the size of the subarray
        - threshold is the mimimum average that is needed to consider subarray
        - get the current sum of the window
        - set it to the max_sum based on threshold
        - iterate through the list starting with k
        - calculate sum based on the current window and check if it is equal or above threshold
        - add the indexes to result list
        """    
        current_sum = sum(arr[:k])
        result = 1 if (current_sum / k) >= threshold else 0
        for i in range(k, len(arr)):
            current_sum = current_sum - arr[i-k] + arr[i]
            if (current_sum / k) >= threshold:
                result += 1
        return result  
```
- initially calculated the current sum
    - this helps reduce processing time
    - not adding this causes the problem TLE
- `current_sum = current_sum - arr[i-k] + arr[i]` -> use current_sum, remove the first element and add current element
