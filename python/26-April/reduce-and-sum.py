class ReduceAndAdd:
    def __init__(self, my_array):
        self.my_array = my_array

    def randomize(self, length):
        import random as rand

        for i in range(length):
            self.my_array.append(rand.randint(0,1))


if __name__ == '__main__':  
    from collections import deque
    """
    sample_array = []
    my_example = ReduceAndAdd(sample_array)
    my_example.randomize(5)
    print(my_example.my_array)
    """

    arr = [1, 1, 0, 1, 1]
    total = 0

    """
    - get the sum of the current array
    - remove the start element
    - iterate through the array
    - get the sum again
    - repeat until element is 1
    - return the sum
    """
    queue = deque(arr)
    while len(queue) != 1:
        total += sum(queue)
        queue.popleft()

    print(total)
    print(queue[0])

