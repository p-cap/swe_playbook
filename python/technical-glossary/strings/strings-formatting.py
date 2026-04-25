"""
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
"""

# strips leading and trailing whitespaces
s = "     supercalifragalisticexpidocious"
print(s)
print(s.strip())

my_string = "               feasfsfrs               "
print(my_string.lstrip())
print(my_string.rstrip())

print('--- replace function ---')
new_string = my_string.replace('f','77777-').strip()
print(new_string)
print('\r\n')
print('--- upper function ---')
upper_string = new_string.upper()
print(upper_string)
print('\r\n')
print('--- lower function ---')
lower_string = new_string.lower()
print(lower_string)

print('--- splitting very important ---')
#  my_string = "               feasfsfrs               "
test_split = my_string.split(' ')
print(test_split)
another_string = 'ghjdghdcgsgcsh'
new_another_string = ''
for ch in another_string:
    if ch.isalpha():
        new_another_string += ch + ' '
print('-- with an space element ---')
print(f'{new_another_string.split(' ')}')
new_another_string = new_another_string[:len(new_another_string) - 1]
my_split = new_another_string.split(' ')
print('--- my split after adding a delimiter ---')
print(my_split)

print('--- using join ---')
print(''.join(my_split))