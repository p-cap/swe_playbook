Dictionaries (Hash Maps) are arguably the most important data structure in DSA because they provide **$O(1)$ average time complexity** for lookups, insertions, and deletions. 

Here is a breakdown of the essential functions and patterns you need to master.

---

### 🛠️ 1. Basic Operations & Access

| Function | Complexity | Use Case |
| :--- | :--- | :--- |
| `d[key] = val` | $O(1)$ | Insertion or update. |
| `d[key]` | $O(1)$ | Access value. **Raises `KeyError`** if key is missing. |
| `d.get(key, default)`| $O(1)$ | Access value safely. Returns `default` if key is missing. |
| `del d[key]` | $O(1)$ | Remove a key-value pair. |
| `key in d` | $O(1)$ | **Membership check.** Essential for avoiding errors. |

> **Trick:** Use `.get()` when you want to avoid `if key in d` checks. For example: `count[char] = count.get(char, 0) + 1`.

---

### 🔄 2. Iteration Patterns
In interviews, you often need to loop through data in different ways.

* **Keys only:** `for key in d:` (This is the default).
* **Values only:** `for val in d.values():`
* **Both (Items):** `for key, val in d.items():` 
    * *Note:* Use this for "Top K Frequent" or "Find the unique element" problems.

---

### 🏗️ 3. Special Dictionary Types (The "Pro" Tools)

#### **`collections.defaultdict`**
This is the most-used tool in DSA. It eliminates the need to check if a key exists before appending to a list or incrementing a counter.
```python
from collections import defaultdict
adj = defaultdict(list)
adj[u].append(v) # No KeyError even if 'u' is new!
```

#### **`collections.Counter`**
A specialized dictionary for counting hashable objects.
```python
from collections import Counter
counts = Counter("abracadabra")
print(counts.most_common(1)) # [('a', 5)]
```



---

### 🧩 4. Dictionary Comprehensions
Useful for transforming data quickly, such as mapping values to their indices.

```python
# Create a map of value -> index
val_to_idx = {val: i for i, val in enumerate(nums)}
```

---

### 🚀 5. Crucial DSA Patterns

#### **Pattern A: The Frequency Map**
Used in almost every string or array problem (Anagrams, Palindrome Permutation).
```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

#### **Pattern B: Hashing for $O(1)$ Lookups (Two Sum)**
Instead of nested loops ($O(n^2)$), use a dictionary to "remember" seen values.
```python
seen = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        return [seen[diff], i]
    seen[num] = i
```



#### **Pattern C: Grouping (Anagrams)**
Use a sorted string or a frequency tuple as a key to group items.
```python
groups = defaultdict(list)
for s in strs:
    key = "".join(sorted(s))
    groups[key].append(s)
```

---

### ⚠️ Common Pitfalls
1.  **Modifying size during iteration:** Never add or remove keys while looping through `d.items()`. This raises a `RuntimeError`. Loop over a list of keys instead: `for k in list(d.keys()):`.
2.  **Memory Usage:** Dictionaries are fast but memory-intensive. If you have a massive range of integer keys (e.g., 1 to 1,000,000), an array `[0] * 1000001` might be more efficient.
3.  **Unhashable Keys:** You cannot use a **List** as a dictionary key because it is mutable. Use a **Tuple** instead.

**Are you working on a specific problem right now where you're deciding between using a Dictionary or a Set?**