# show how heapq.heapify works
import heapq

def my_heappop():
    # popping data from min_heap
    if len(data) > k:
        heapq.heappop(data)

if __name__ == "__main__":
    k = 3
    data =  [4, 5, 8, 2]
    print(f"Original: {data}")
    print(f"k: {k}")

    # heapifying the min_heap
    heapq.heapify(data)
    print(f"After heapify: {data}")

    # pop from the heap
    my_heappop()

    print(f"After the first pop: {data}")
    # pushing data onto min_heap
    stream_data = 3
    print(f"Adding {stream_data}")
    heapq.heappush(data, stream_data)
    print(f"After heapush: {data}")

    # pop from the heap
    my_heappop()
    
    # return the root of the heap
    print(f"After heappop: {data}")
    print(data[0])
