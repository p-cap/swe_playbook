from collections import defaultdict
u = 'first'

adj = defaultdict(list)
adj[u].append('una')

#  defaultdict(<class 'list'>, {'first': ['una']})
print(adj)

my_defaultdict = defaultdict(int)
my_string = 'cdushciudhuihvdsiuhducvdish'

for i in my_string:
    my_defaultdict[i] += 1


## Dictionary comprehension
val_to_idx = { index: value for index, value in enumerate(my_defaultdict.values())}
print(val_to_idx)

# frequency map
counts = {}
for letter in my_string:
    # NOTE: When using the get method, we'll need the default return which is 0
    counts[letter] = counts.get(letter, 0) + 1
    
print(counts)

# testing get function with defaultdict
another = defaultdict(int)
key = 'wassup'
# this causes a TypeError because the operand types are incompatible
# in this case, because the key DOES NOT EXISTS, therefore adding a NoneType and int is not valid
# another[key] = another.get(key) + 1

# to solve this issue, we need to add the default return for the get function
another[key] = another.get(key,0) + 1
print(another)