s = "pwwkew"
window = set()
left, right = 0, 0
n = len(s)
longest = 1

for right in range(n):
    while s[right] in window:
        window.remove(s[left])
        left += 1
    
    window.add(s[right])
    longest = max(longest, right - left + 1)
print(longest)
print(window) 