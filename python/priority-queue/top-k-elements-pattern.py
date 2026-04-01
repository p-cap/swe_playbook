from collections import Counter
import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2

# 1. instantiate Counter library to easily create a frequency map
count = Counter(nums)

# 2. initialize min_heap list
min_heap = []

# 3. iterate through Counter using .items()
for num, freq in count.items():

    # 4. Add elements to min_heap as tuple between the freq and num
    heapq.heappush(min_heap, (freq, num))
    
    # 5. pop from min_heap if it is larger than k
    if len(min_heap) > k:
        heapq.heappop(min_heap)

# 6. Cast the for loop into an iterable to get the result
result = [val for freq, val in min_heap]
print(result)

