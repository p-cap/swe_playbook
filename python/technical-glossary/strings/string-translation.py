"""
### 🧮 4. Translation & Character Math
For many "String to Integer" or "Cipher" problems, you need to work with ASCII values.

* **`ord(char)`**: Converts a character to its ASCII/Unicode integer (e.g., `ord('a')` is 97).
* **`chr(int)`**: Converts an integer back to a character (e.g., `chr(97)` is 'a').
* **Mapping Pattern:** To map 'a'-'z' to 0-25: `index = ord(char) - ord('a')`.

---
"""

my_string = 'gchdsgbhagdcuihsabdh'
my_sum = 0
for i in my_string:
    my_sum += ord(i) - ord('a')
# print(my_sum)

num_string = 6768784908123490732858934

# we need to calculate window
window = len(str(num_string)) - 2 + 1
my_char = ''
# while (num_string != 0):
#     my_char += chr(num_string % 100)
#     num_string //= 100

# for char in my_char:
#     if char == ' ':
#         # space is 32
#         print(ord(char))

# for i in str(num_string):
#     my_int = int(i)
#     print(my_int)
    
freq_map = [0] * 26

for i in my_string:
    index = ord(i) - ord('a')
    print(f"index: {index}")
    freq_map[index] += 1
print(freq_map)

