import heapq

stones = [2,7,4,1,8,1]

# 1. turn the list into max_heap
max_heap = [-i for i in stones]
heapq.heapify(max_heap)

# 2. Pop from max_heap until length of max heap is greater than 1
while len(max_heap) > 1:
    first_stone = heapq.heappop(max_heap)
    second_stone = heapq.heappop(max_heap)
    
    # 2a. Calculate the difference between first and second stone
    # then push it max_heap
    if first_stone != second_stone:
        heapq.heappush(max_heap, first_stone - second_stone)

# 3. if the beginning of max_heap exists, return the ONLY element 
# other return 0
print(-max_heap[0] if max_heap else 0)