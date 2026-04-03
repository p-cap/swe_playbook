# Priority Queue (Heap) Master Guide

## Coding Strategy
* select a leetcode problem based on the pattern
* Ask `Gemini` for a solution
* Validate the solution in leetcode
* IMPORTANT: Read and heed the problem
* solve it locally as `.py` or `.ipynb`
* Comment through out the code 
* IMPORTANT: solve it in leetcode platform without looking
* IMPORTANT: the doubts in recalling the code will field FAQs
* Generate FAQs about the problem (where to put it????)


## 🚀 Master Logic Table (Quick Reference)

| Strategy | Trigger Words | Selection Logic (The "Why") | Key LeetCode |
| :--- | :--- | :--- | :--- |
| **Top K Elements** | "Top K," "Kth largest," "K closest," "K frequent" | **Min-Heap** for Top K Largest (pop the smallest "losers"). | 347, 215, 973 |
| **Two Heaps** | "Median," "Stream," "Continuous," "Middle element" | **Max-Heap** (left half) + **Min-Heap** (right half). | 295, 480 |
| **K-Way Merge** | "Merge K lists," "Sorted streams," "Smallest range" | **Min-Heap** stores the "heads" of all $K$ sorted sources. | 23, 632 |
| **Greedy Simulation** | "Min cost," "Connect sticks," "Last stone," "Optimize" | **Min-Heap** to repeatedly combine the two smallest items. | 1046, 1167 |
| **Task Scheduling** | "Meeting rooms," "CPU," "Intervals," "Finish times" | **Min-Heap** stores "End Times" to find the next available slot. | 253, 1834 |

---
## 1. Top K Elements Pattern
**Goal:** Find the $K$ largest, smallest, or most frequent elements in a dataset of size $N$.

* **Logic (K Largest):** Use a **Min-Heap**. Iterate through elements. If the heap size exceeds $K$, `heappop()`. The root (smallest) is removed, leaving only the "largest" candidates.0
* **Time Complexity:** $O(N \log K)$
* **Space Complexity:** $O(K)$

### 347. Top K Element Pro tip and FAQs
Source: `python\priority-queue\top-k-elements-pattern.py`

When is `print(f'count')` become an error?
> Versions lower than `Python 3.6` did not support `f string`
 
 How is a list of tuples heapified?
 > the `first element` in the tuple is what's being utilized

 Why does the default `heapq` behavior work for this problem?
 > the root of the heap will be the minimum value amongst the elements in the list. When we pop an element using heappop(), we removing the root of the list meaning element zero in the list

### CODE
```
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
```

---

## 2. Two Heaps Pattern (Median Finder)
**Goal:** Find the median of a data stream where numbers are constantly being added.

* **Logic:**
    * **Max-Heap (Small Half):** Stores the smaller half of numbers.
    * **Min-Heap (Large Half):** Stores the larger half of numbers.
* **Strategy:** Keep the heaps balanced (size difference $\le 1$). The median is either the top of the larger heap or the average of both tops.
* **Complexity:** $O(\log N)$ to add, $O(1)$ to find median.

### 295. Find Median from Data Stream Pro tips and FAQs
Does `max_heap[0]` and `val = heapq.heappop(max_heap)` return the same value?
> the difference is between access and removal. max_heap[0] is an O(1) operation while heapq.heappop(...) is a O(log N) operation

If we want to return a float that when dividing two numbers, using `/` true division is enough

```
import heapq

# create the MedianFinder class
class MedianFinder:
    def __init__(self):
        # max_heap for the lower half
        self.small = []

        # min_heap for the upper half
        self.large = []

        # the max_heap of the lower half and the min_heap of the upper half is essentially looking for the median 
    
    def addNum(self, num):
        # for the small half, we are creating a max heap due to setting the negative number
        heapq.heappush(self.small, -num)

        # make sure every number in small <= every num in large
        # in this case, we are adding the negative number again to make it positive
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappop(self.large, val)

        # is the difference between the two heaps 2 or more?
        # Which ever half has the extra element will have its element popped
        # and the popped element will be moved to the half with fewer elements
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0
```
---

## 3. K-Way Merge Pattern
**Goal:** Merge $K$ sorted arrays, linked lists, or streams into one sorted result.

* **Logic:** 1. Push the first element of each of the $K$ lists into a **Min-Heap**.
    2. Pop the smallest element (the overall minimum).
    3. Push the *next* element from that specific source list into the heap.
* **Complexity:** $O(N \log K)$ (where $N$ is total elements).

---

## 4. Minimum Cost / Greedy Simulation
**Goal:** Repeatedly combine the two "best" (smallest/largest) items to find an optimal sum or result.

* **Logic:** 1. `heapify()` the entire list ($O(N)$).
    2. While `len(heap) > 1`, pop the two smallest items.
    3. Process them (e.g., sum them) and push the result back.
* **Complexity:** $O(N \log N)$.

---

## 5. Interval / Task Scheduling Pattern
**Goal:** Manage overlapping intervals or schedule tasks based on start/end times.

* **Logic:** Sort the input by start time. Use a **Min-Heap** to store the **end times** of active tasks. The top of the heap tells you which task finishes soonest.
* **Complexity:** $O(N \log N)$.

---

## Cheat Sheet: Python `heapq` Reference

| Operation | Logic | Code Example |
| :--- | :--- | :--- |
| **Initialize** | Transform list in-place ($O(N)$) | `heapq.heapify(nums)` |
| **Min-Heap** | Default behavior (Smallest at root) | `heapq.heappush(h, val)` |
| **Max-Heap** | Negate values (Largest at root) | `heapq.heappush(h, -val)` |
| **Custom Priority**| Use Tuples `(priority, item)` | `heapq.heappush(h, (freq, word))` |
| **Top K Shortcut** | Efficient built-in utility | `heapq.nlargest(k, nums)` |

> **Pro-Tip:** In BFS/Dijkstra problems, the Priority Queue stores `(distance, node)`. This ensures you always process the shortest path first.