"""
### 🧩 2. Slicing Power Tricks
Slicing is Python’s "cheat code" for array manipulation.
`syntax: arr[start:stop:step]`

* **Reverse an array:** `arr[::-1]`
* **Shallow Copy:** `arr[:]`
* **Extract every 2nd element:** `arr[::2]`
* **Rotate an array to the left by $k$:** `arr[k:] + arr[:k]`
* **Safe Sub-array:** `arr[i:j]` (Note: Does not throw an error if $j > \text{len(arr)}$).

---
"""

my_array_two = [21, 87, 53, 16, 21, 43, 93, 5, 97, 32]
print(my_array_two[::-1])

test_every_second_element = []
starting_index = 1
for i in range(starting_index, 11):
    if i % 2 == 0:
        test_every_second_element.append('wassup!')
    else: 
        test_every_second_element.append('?')
# the slice starts at 0
# but we can change the starting index in this case
test_every_second_element = test_every_second_element[starting_index::2]
print(test_every_second_element)

print('-- rotating array based on the given index --')
print(my_array_two)
k = 3
# k as starting point to end and starting to k
print(my_array_two[k:] + my_array_two[:k])
