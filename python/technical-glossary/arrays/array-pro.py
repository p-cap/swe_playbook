"""
---

### 🚀 5. DSA "Pro" Patterns

#### **The Two-Pointer Swap**
Common in "Reverse String" or "Sort Colors" problems.
```python
arr[l], arr[r] = arr[r], arr[l]
```

#### **The `enumerate()` Loop**
Use this when you need both the **index** and the **value** (almost always).
```python
for i, val in enumerate(nums):
    if val == target: return i
```

#### **The `zip()` Function**
Iterate through two arrays simultaneously.
```python
for a, b in zip(list1, list2):
    print(a + b)
```

"""

my_string = 'gorilla'
n = len(my_string)
arr = []

for i in my_string:
    arr.append(i)

print(arr)
print('-----------------------------')

# for i in range(1,n,2):
#     print(i)    
#     arr[i - 1], arr[i] = arr[i], arr[i - 1]
#     print(arr)
#     print('-----------------------------')

# using the combination of defaultdict and enumerate to build frequency map
from collections import defaultdict

freq_map = defaultdict(int)

for index,value in enumerate(arr):
    freq_map[value] += 1
print(freq_map)

print('--- using zip ---')
import random 
lst1 = [True, False, True, False, False, False, False]
lst2 = []
for i in range(len(lst1)):
    lst2.append(i)

my_dict = defaultdict(bool)

for a,b in zip(lst1, lst2):
    my_dict[b] = a

print(my_dict)