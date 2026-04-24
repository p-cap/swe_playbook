### Strings In Python
In Python, strings are **immutable**, meaning every transformation creates a **new** string

### 🔍 1. Searching & Boolean Checks
These are essential for validating input or finding substrings without manually looping through characters.

| Function | Description | Logic / Use Case |
| :--- | :--- | :--- |
| `s.find(sub)` | Returns the lowest index of `sub`. Returns `-1` if not found. | Finding the start of a pattern. |
| `s.index(sub)` | Same as `find`, but raises a `ValueError` if not found. | Use when you **expect** the substring to exist. |
| `s.startswith(pre)` | Returns `True` if string starts with `pre`. | Prefix problems (e.g., Longest Common Prefix). |
| `s.endswith(suf)` | Returns `True` if string ends with `suf`. | File extension or suffix validation. |
| `s.isalpha()` | `True` if all characters are letters. | Filtering out noise in Palindrome problems. |
| `s.isalnum()` | `True` if all characters are letters or numbers. | Clean input for "Valid Palindrome." |
| `s.isdigit()` | `True` if all characters are numbers. | String-to-Integer conversion (Atoi). |

---

### ✂️ 2. Formatting & Transformation
Since strings are immutable, these functions return a **copy** of the string.

* **`s.strip()` / `s.lstrip()` / `s.rstrip()`**: Removes whitespace (or specific characters) from the ends. Crucial for "Reverse Words in a String."
* **`s.lower()` / `s.upper()`**: Case normalization. Always normalize case before comparing characters for equality.
* **`s.replace(old, new, count)`**: Replaces occurrences of a substring. The `count` parameter is helpful if you only want to replace the first $N$ instances.
* **`s.split(sep)`**: Breaks a string into a **List**. This is the most common first step for word-based problems.
* **`sep.join(iterable)`**: The efficient way to build a string from a list. 

> **💡 Efficiency Tip:** Never use `s += char` inside a loop. This is $O(N^2)$ because a new string is created every time. Instead, append characters to a **List** and use `"".join(list)` at the end for $O(N)$ performance.

---

### 🧩 3. Advanced Slicing (The Python Superpower)
Slicing is often more powerful than any built-in function in Python. The syntax is `s[start:stop:step]`.

* **`s[::-1]`**: Reverses a string in $O(N)$ time.
* **`s[k:] + s[:k]`**: Rotates a string by $k$ positions.
* **`s[i:j]`**: Extracts a substring from index $i$ to $j-1$.

---

### 🧮 4. Translation & Character Math
For many "String to Integer" or "Cipher" problems, you need to work with ASCII values.

* **`ord(char)`**: Converts a character to its ASCII/Unicode integer (e.g., `ord('a')` is 97).
* **`chr(int)`**: Converts an integer back to a character (e.g., `chr(97)` is 'a').
* **Mapping Pattern:** To map 'a'-'z' to 0-25: `index = ord(char) - ord('a')`.

---

### 🛠️ 5. Frequent Coding Patterns

#### **Frequency Counter**
Use `collections.Counter` to find character frequencies in $O(N)$.
```python
from collections import Counter
s = "anagram"
counts = Counter(s) # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
```

#### **The Sliding Window Template**
Many string problems (e.g., "Longest Substring Without Repeating Characters") use this logic:

```python
left = 0
char_set = set()
for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
```

#### **Two-Pointer Palindrome Check**
```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l, r = l + 1, r - 1
    return True
```

**Which of these string patterns do you find most difficult to implement in a timed environment?**