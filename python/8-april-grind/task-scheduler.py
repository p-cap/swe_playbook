from collections import Counter, deque
import heapq

tasks = ["A","A","A","B","B","B"]
n = 2

counts = Counter(tasks)

# why take the values
# why max heap?
max_heap = [-cnt for cnt in counts.values()]
heapq.heapify(max_heap)

time = 0

queue = deque()

while max_heap or queue:
    time += 1
    
    if max_heap:
        
        cnt = heapq.heappop(max_heap) + 1

        if cnt != 0:
            queue.append([cnt, time + n])
    
    if queue and queue[0][1] == time:
        heapq.heappush(max_heap, queue.popleft()[0])

print(time)