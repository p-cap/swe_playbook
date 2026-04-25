"""
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
"""

"""
# checks for ALL characters
# this returns true
s = "supercalifragalisticexpidocious"
print(s.isalpha())

# checks if all characters are letter
# this returns false
s_with_num = "45ggcesghiab"
print(s_with_num.isalpha())

# checks if all characters are alpha and numbers
s_digit = "6378468763874637"
print(s_digit.isalnum())
"""

"""s.endswith(letter)
s = "supercalifragalisticexpidocious"
letter = 't'
# s.endswith(letter)  does not throw an exception
print(s.endswith(letter))
"""

"""s.startswitha()
s = "supercalifragalisticexpidocious"
letter = 't'

# s.startswith(letter)  does not throw an exception
print(s.startswith(letter))
"""
"""s.find()

import traceback

try:
    s = "supercalifragalisticexpidocious"
    my_char = 'xnaklescnsaeklncsa'
    print(s.index(my_char))
    print(s.index(my_char) == s.find(my_char))

# raise for intentional purpose
except Exception as e:
    print("--- the exception is ---")
    traceback.print_exc()


# if not string is found, a ValueError is thrown
Traceback (most recent call last):
  File "/Users/pckap/mssa/swe_playbook/python/technical-glossary/strings-demo.py", line 18, in <module>
    print(s.index(my_char))
          ~~~~~~~^^^^^^^^^
ValueError: substring not found
"""



"""s.find()
s = "supercalifragalisticexpidocious"
chosen_letter = 'dasjndoaes'
found_letter = s.find(chosen_letter)
print(f"s.find(chosen_letter): {found_letter}")

# let's find the second instance of the find method
found_another = s.find(chosen_letter, found_letter + 1)
print(f"found_another: {found_another}")

from collections import Counter

def validate_common(my_string):
    count_s = Counter(my_string)
    for key,value in count_s.most_common():
        # print(f"{key} : {value}")
        chosen_key = key
        chosen_value = value
        break;
    i = 0
    check_value = set();
    while my_string.find(chosen_key, i) != -1:
        if my_string.find(chosen_key, i) != -1:
            check_value.add(my_string.find(chosen_key, i))
        ret = my_string.find(chosen_key, i)
        i += 1
  
     
    # print(f"check_value == value: {check_value == value}")
    return ret, len(check_value) == value

last_index, is_most_common = validate_common(s)
print("--- Last idnex for most common")
print(last_index)
print("--- is check_value the same as .most_common function ---")
print(is_most_common)
"""





"""
s.find(chosen_letter): -1
found_another: -1
<class 'str'>
-1

while my_string.find(chosen_key, i) != -1:
        i += 1
        ret = my_string.find(chosen_key, i)

this returns -1
"""