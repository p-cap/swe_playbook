import heapq
    # using the heapq library
nums = [4, 5, 8, 2]
print(f'nums: {nums}')
heapq.heapify(nums)
print(f'nums: {nums}')

k = 3
if len(nums) > k:
    # popping the root of the min_heap
    heapq.heappop(nums)
print(f'After pop, it looks like: {nums}')