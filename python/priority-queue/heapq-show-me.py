# show how heapq.heapify works
import heapq

k = 4
data =  [4, 5, 8, 2]
print(f"Original: {data}")
print(f"k: {k}")

# heapifying the min_heap
heapq.heapify(data)
print(f"After heapify: {data}")

# pushing data onto min_heap
stream_data = 3
print(f"Adding {stream_data}")
heapq.heappush(data, stream_data)
print(f"After heapush: {data}")

# popping data from min_heap
if len(data) > k:
    heapq.heappop(data)

# This does not represent 
print(f"After heappop: {data}")
print(data[0])