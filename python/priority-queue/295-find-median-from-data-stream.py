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
        
