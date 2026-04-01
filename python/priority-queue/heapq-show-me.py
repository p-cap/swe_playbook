# show how heapq.heapify works
import heapq

# 1. Start with an unsorted list
data = [10, 1, 5, 20, 2]
print(f"Original: {data}")

# 2. transforms list into a heap
heapq.heapify(data)
print(f"After heapify: {data}") # not fully sorted BUT data[0] is the smallest

smallest = heapq.heappop(data)
print(f"Popped the smallest: {smallest}")
print(f"Data after the pop is: {data}")

heapq.heappush(data, 3) # 3 is the second element
print(f"After pushing 3: {data}")
