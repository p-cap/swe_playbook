"""
### ⚡ 3. Initialization Tricks

**1D Array of size $N$ with zeros:**
```python
arr = [0] * n
```

**2D Array (Matrix) of size $R \times C$:**
* **❌ Wrong:** `[[0] * c] * r` (This creates references to the *same* list! Changing one row changes all).
* **✅ Right:** `[[0] * c for _ in range(r)]`

---
"""

arr = [0] * 6
print(arr)

# 2d matrix
r = 3
c = 3
my_matrix = [[0] * c for _ in range(r)]
print(my_matrix)