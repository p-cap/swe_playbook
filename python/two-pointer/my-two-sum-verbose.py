from collections import defaultdict

"""
- iniatialize a default_dicy by setting the nums index as the key 
- extract the values from the dictionary
- grab the values from from the num_dict
- sort the values array NOTE: I see quite frequently that the values are already sorted
- use TWO POINTER to check if the sum of the two pointers match target
- appends the values onto another list that saves the keys
- enumerate through the dictionary grabbing the key and value
- check if the value is in the values collected from the two pointer operation, add its key to the result list
- return the result list 
"""
class Solution:
    def twoSum(self, nums, target):
        nums_dict = defaultdict(int)
        size = len(nums)
        result = []
        for i in range(size):   
            nums_dict[i] = nums[i]
        
        values = [val for val in nums_dict.values()]
        left = 0
        right = len(values) - 1
        values_from_keys = []
        
        values.sort()
        while left < right:
            two_sum = values[left] + values[right]
            if two_sum == target:
                values_from_keys.append(values[left])
                values_from_keys.append(values[right])
                break
            elif two_sum > target:
                right -= 1
            else:
                left += 1
        
        for key,val in nums_dict.items():
            if val in values_from_keys:
                result.append(key)
        
        return result

my_solution = Solution()
nums = [3,3]
target = 6
result = my_solution.twoSum(nums, target)
print(result)