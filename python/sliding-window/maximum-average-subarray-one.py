nums = [1,12,-5,-6,50,3] 
k = 4

current_sum = sum(nums[:k])
max_average = current_sum / k

for i in range(k,len(nums)):
    current_sum = current_sum - nums[i-k] + nums[i]
    max_average = max(max_average, current_sum / 4)
            
print(max_average)