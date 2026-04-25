"""
---

### 🧩 3. Advanced Slicing (The Python Superpower)
Slicing is often more powerful than any built-in function in Python. The syntax is `s[start:stop:step]`.

* **`s[::-1]`**: Reverses a string in $O(N)$ time.
* **`s[k:] + s[:k]`**: Rotates a string by $k$ positions.
* **`s[i:j]`**: Extracts a substring from index $i$ to $j-1$.

---
"""
# reversing the string
s = "     supercalifragalisticexpidocious"
print(s[::-1])

# rotates string with k position
rotate_me = "wwwwwwwirrrrrrrr"
print(rotate_me)
k = rotate_me.find('i')
print(rotate_me[k:] + rotate_me[:k])


print('--- slicing basics ----')
# slicing 
see_me = "cjnaklwassupdase;kfl;aske"
w = see_me.find('w')
p = see_me.find('p')
# print(w)
# print(p)
print(f"{see_me[w:p+1]}???")
