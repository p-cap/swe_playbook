## Sliding Window Pattern

### Fixed Size Window
- Calculate the sum/state of the first $K$ elements.
- Iterate from $K$ to $N$.
- New State = Old State + arr[right] - arr[right - K].

#### 643. Maximum Average Subarray I
- python/sliding-window/maximum-average-subarray-one.py
- `current_sum = sum(nums[:k])` -> we calculate the sum/state of the first K elements
- `for i in range(k,len(nums)):` -> we iterate starting from K to len(nums)
- ``current_sum = current_sum - nums[i-k] + nums[i]` -> we remove the first element of the last window and add the current element of the current window

#### 1456. Maximum Number of Vowels in a Substring of Given Length
- Calculate the first k elements to determine the number of vowels
```python
for i in range(k):
    count += int(s[i] in vowels)
```
- Iterate from $K$ to $N$
```python
for i in range(k, len(s)):
```
- Shifting the window
```python
# the count decrements if the beggining of the window is a vowel
count -= int(s[i - k] in vowels)
    
# increments if the new element entering the window is a vowel
count += int(s[i] in vowels)
```

#### 567. Permutation in String
- PATH: python/sliding-window/permutation-in-string.py
- Calculate the first K elements to see if s2 has a permutation of s1 in the window_count
- We'll need to check if the current_window matched s1_count
```python
n1, n2 = len(s1), len(s2)

s1_count = [0] * 26
window_count = [0] * 26

for i in range(n1):
    s1_count[ord(s1[i]) - ord('a')] += 1
    window_count[ord(s1[i]) - ord('a')] += 1

if s1_count == window_count:
    return True
```
- Iterate from $K$ to $N$
```python
for i in range(k, n2):
    window_count[ord(s2[i - n1]) - ord('a')] -= 1
    window_count[ord(s2[i]) - ord('a')] += 1
    if window_count == s1_count:
        return True
```

### Dynamic Window: Finding the Longest
- Expand the right pointer to include a new element.
- Check if the window is still valid.
- If invalid (e.g., too many unique characters), move left forward until it becomes valid again.
- Update the max_length at each step where the window is valid.
- ALWAYS REMEMBER, WE REMOVE THE BEGINNING OF THE WINDOW
- we are using hashset as the window

#### 3. Longest Substring Without Repeating Characters
- Expand the right pointer to include a new element
    - the window is handled by hashset
    - the rigut pointer elmenet is always added to the hashset
    - `seen_chars.add(s[right])` is the new character added window aka hashset
```python
        for right in range(len(s)):
            # If we find a duplicate, the window is INVALID
            # Shrink from the left until the duplicate is removed
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            
            # Add the new character to the window
            seen_chars.add(s[right])
```
- Check if the window is still valid
    - the right char is in the window, we remove the LEFT element
    - increment left by 1
```python
for right in range(len(s)):
    # If we find a duplicate, the window is INVALID
    # Shrink from the left until the duplicate is removed
    while s[right] in seen_chars:
        seen_chars.remove(s[left])
        left += 1
```
- If invalid (e.g., too many unique characters), move left forward until it becomes valid again.
    - because right is in the window, we REMOVE THE LEFT ELEMENT
    - we increment the left 
```python
for right in range(len(s)):
    # If we find a duplicate, the window is INVALID
    # Shrink from the left until the duplicate is removed
    while s[right] in seen_chars:
        seen_chars.remove(s[left])
        left += 1
```
- Update the max_length at each step where the window is valid.
    - the previous while statement checks if right element is in the window
    - the max is always upadated based on the left and right pointer
```python
max_length = max(max_length, right - left + 1)
```

#### 424. Longest Repeating Character Replacement
- python/sliding-window/424-longest-repeating-character-replacement.py
- Expand the right pointer to include a new element
    - the right will iterate through regardless
    - the inclusion of elements is tracking the frequency of the elements in a hashmap
```python
for right in range(len(s)):
    count[s[right]] = 1 + count.get(s[right], 0)
    max_freq = max(max_freq, count[s[right]])
```
- Check if the window is still valid
    - window is no longer valid if there is not enough k
```python
while (right - left + 1) - max_f > k
```
- Update the max_length at each step where the window is valid
    - max is taken based on the frequency of the char
```python
max_freq = max(max_freq, count[s[right]])
```
#### 1004. Max Consecutive Ones III


### Finding the shortest
#### 209. Minimum Size Subarray Sum:
#### 76. Minimum Window Substring