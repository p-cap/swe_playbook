s1 = "ab"
s2 = "eidbaooo"
n1, n2 = len(s1), len(s2)
result = True
if n1 > n2: result = False

# Initialize frequency list
# frequency map is for tracking characters
s1_count = [0] * 26
window_count = [0] * 26

# build the frequency map for s1_count
# build the frequency map for window_count
for i in range(n1):
    s1_count[ord(s1[i]) - ord('a')] += 1
    window_count[ord(s2[i]) - ord('a')] += 1
    
# this checks if the first window contains permutation
if s1_count == window_count:
    print(True)

# slide the window across s2
for i in range(n1, n2):
    # add the new character
    window_count[ord(s2[i]) - ord('a')] += 1
    
    # remove the old character
    # ord(s2[i - n1])
    # ord(s2[i - n1]) = ord(s2[2 - 2]) = ord(s2[0])
    # ord(s2[0]) - ord('a')
    window_count[ord(s2[i - n1]) - ord('a')] -= 1
    
    if s1_count == window_count:
        print(True)
        break