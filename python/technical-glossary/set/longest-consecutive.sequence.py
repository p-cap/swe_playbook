nums = [100,4,200,1,3,2]

# The set is crucial because sorting is not needed
num_set = set(nums)
longest = 0
print(num_set)
for i in num_set:
    if i - 1 not in num_set:
        length = 1
        
        while i + length in num_set:
            length += 1
        
        longest = max(longest, length)

print(longest)