s = "AABABBA"
k = 1

count = {}
result = 0
left = 0
max_freq = 0
n = len(s)

for right in range(n):
    # add the char to count to create frequency counter
    count[s[right]] = 1 + count.get(s[right], 0)
    
    # check max freq for the number of chars
    max_freq = max(max_freq, count[s[right]])
    
    # the difference between the current window and the current max freq
    while (right - left + 1) - max_freq > k:
        # remove the left char
        count[s[left]] -= 1
        
        # move the left pointer
        left += 1
    
    result = max(result, right - left + 1)

print(result)