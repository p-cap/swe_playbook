s = "pwwkew"
longest = 0
left = 0
n = len(s)
char_set = set()

for right in range(n):
    # use while to check for all instances of the right
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    longest = max(longest, right - left + 1)
print(longest)



