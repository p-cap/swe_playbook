
Python lists are dynamic arrays, making them incredibly versatile for DSA. Here is a curated list of essential functions, slicing tricks, and optimization patterns you’ll use in almost every problem.

---

### 🛠️ 1. Essential Built-in Functions

| Function | Time Complexity | Use Case |
| :--- | :--- | :--- |
| `arr.append(x)` | $O(1)^*$ | Add to the end. |
| `arr.pop()` | $O(1)$ | Remove from the end (Stack behavior). |
| `arr.pop(0)` | $O(n)$ | Remove from the start (**Warning:** Very slow, use `deque` instead). |
| `arr.insert(i, x)`| $O(n)$ | Insert at index `i`. |
| `arr.sort()` | $O(n \log n)$ | Sorts in-place. |
| `sorted(arr)` | $O(n \log n)$ | Returns a **new** sorted list. |
| `reverse()` | $O(n)$ | Reverses in-place. |

---

### 🧩 2. Slicing Power Tricks
Slicing is Python’s "cheat code" for array manipulation.
`syntax: arr[start:stop:step]`

* **Reverse an array:** `arr[::-1]`
* **Shallow Copy:** `arr[:]`
* **Extract every 2nd element:** `arr[::2]`
* **Rotate an array to the left by $k$:** `arr[k:] + arr[:k]`
* **Safe Sub-array:** `arr[i:j]` (Note: Does not throw an error if $j > \text{len(arr)}$).

---

### ⚡ 3. Initialization Tricks

**1D Array of size $N$ with zeros:**
```python
arr = [0] * n
```

**2D Array (Matrix) of size $R \times C$:**
* **❌ Wrong:** `[[0] * c] * r` (This creates references to the *same* list! Changing one row changes all).
* **✅ Right:** `[[0] * c for _ in range(r)]`

---

### 🔎 4. Searching & Filtering

* **Find Index:** `arr.index(value)` ($O(n)$, raises `ValueError` if missing).
* **Count Occurrences:** `arr.count(value)` ($O(n)$).
* **Check Existence:** `if x in arr:` ($O(n)$ for lists, $O(1)$ for sets).
* **List Comprehension Filter:** `evens = [x for x in nums if x % 2 == 0]`

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

---

### 📦 6. Beyond the Basic List
When the standard list is too slow, use these:

1.  **`collections.deque`**: For $O(1)$ pops and appends from **both** ends (Queues/BFS).
2.  **`heapq`**: For Priority Queues (Min-Heaps).
3.  **`bisect`**: For Binary Search on a sorted array.
    * `bisect.bisect_left(arr, x)`: Finds the first index to insert `x` to maintain order.

---

### ⚠️ Common DSA Pitfalls
1.  **Removing while looping:** Never use `arr.remove(x)` or `del arr[i]` inside a `for` loop over that same array. It skips elements. Use a new list or loop backwards.
2.  **List Concatenation:** `list1 + list2` creates a brand new list ($O(n+m)$). If you just want to add elements, use `list1.extend(list2)`.
3.  **Large Pops:** If a problem requires frequently removing the first element, **stop using a list.** A list `pop(0)` is $O(n)$; a `deque.popleft()` is $O(1)$.

