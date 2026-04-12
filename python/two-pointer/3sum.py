nums = [-1,0,1,2,-1,-4]
expected = [[-1,-1,2],[-1,0,1]]
result = []

def two_sum(result, nums, first):
    left = first + 1
    right = len(nums) - 1
    
    while left < right:
        my_sum = nums[first] + nums[left] + nums[right]
        if my_sum > 0:
            right -= 1
        elif my_sum < 0:
            left += 1
        else:
            result.append([nums[first], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
    return result


if __name__ == '__main__':
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        
        # avoid duplicate 
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # I WAS PASSING THE INDEX INSTEAD OF THE VALUE
        two_sum(result, nums, i)
    print(result)