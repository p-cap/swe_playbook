from collections import defaultdict

my_defaultdict = defaultdict(int)
my_string = 'cdushciudhuihvdsiuhducvdish'

for i in my_string:
    my_defaultdict[i] += 1

print('--- defaultdict test case ---')
print(my_defaultdict)

max_val = -1
leaders = []

# let's account for ties
for key, val in my_defaultdict.items():
    if val > max_val:
        max_val = val
        # once a new max is found, we re-initialize the list
        leaders = [key]
    elif val == max_val:
        leaders.append(key)
print(leaders)
"""
We built an algorithm that checks for the max value with the given defaultdict. We start with initializing the max_val that obviously stores max_val and the leaders list that stores the most frequent keys. Then, we iterate through the dictionary using the items() function. Inside the for loop, we check the current value and max_val. If the current value is greater than the max value, we set the current value as the max value. Also, one of the key features of this algorithm is initializing the keys list. Why? Because everytime a new max value is encounter, the leaders array ensures only the leading characters are stored in the list. Another condition is if the current value is the same as the max value. If so, we append the key to the leaders list. This is another key feature because it stores other keys of the same value. We return the leaders list containing all the keys that are the most frequent
"""
