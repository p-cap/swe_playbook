from collections import defaultdict

my_defaultdict = defaultdict(int)
my_string = 'cdushciudhuihvdsiuhducvdish'

for i in my_string:
    my_defaultdict[i] += 1



def find_max_from_dict():
    max_val = 0
    for key, val in my_defaultdict.items():
        max_val = max(max_val, val)

    for key, val in my_defaultdict.items():
        if val == max_val:
            print(f'{key} : {val}')


# use the max function
# this does not account for tie
max_char = max(my_defaultdict, key=my_defaultdict.get)
print(f'max_char using the max function: {max_char}')


from collections import Counter
count = Counter(my_defaultdict)
print(count)
top_char, top_val = count.most_common(1)[0]
print('--- instantiated defaultdict with Counter and calling the most_common function ---')
print(f'{top_char} : {top_val}')

# this will account for duplicate top frequency values
max_val = -1
leaders = []

for key, val in my_defaultdict.items():
    if val > max_val:
        max_val = val
        # this apparently starts with the a new list
        leaders = [key]
    elif val == max_val:
        leaders.append(key)

for char in leaders:
    print(f'{char} : {max_val}')        

print('--- getting i ---')
print(f'i: {my_defaultdict.get('i')}')
print('--- getting z and returns a None ----')
print(f'z: {my_defaultdict.get('z')}')

print('--- check key in my_defaultdict')
print('i' in my_defaultdict)
print('z' in my_defaultdict)

