"""
### 🔎 4. Searching & Filtering

* **Find Index:** `arr.index(value)` ($O(n)$, raises `ValueError` if missing).
* **Count Occurrences:** `arr.count(value)` ($O(n)$).
* **Check Existence:** `if x in arr:` ($O(n)$ for lists, $O(1)$ for sets).
* **List Comprehension Filter:** `evens = [x for x in nums if x % 2 == 0]`

---
"""
import random
my_array = []
# for i in range(11):
#     my_array.append(random.randint(1,99))
my_array = [47, 80, 99, 94, 5, 94, 32, 31, 68, 89, 41]

print(my_array.index(31))

# print(my_array.index(67))
# this can help handle the ValueError exception
if 67 in my_array:
    print(my_array.index(67))
else:
    print("protecting the exception from the index function")
    
# list comprehension filter
test_array = [i for i in my_array if i > 67]
print(test_array)


