"""
return the number of combinations based on the k

def backtrack(start, path):
    # let's reference the output variable being global
    if len(path) == k:
        output += 1
        return
    for i in range(start, len(my_string_arr)):
        path.append(my_string_arr[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, path)
print(output)

backtracking-returning-variables.py", line 17, in backtrack
    output += 1
    ^^^^^^
UnboundLocalError: cannot access local variable 'output' where it is not associated with a value

# this error occurs even though we have global output variable
# output is not recoginized 
"""

"""
def backtrack(start, path):
    output = 0
    # let's reference the output variable being global
    if len(path) == k:
        output += 1
        return
    for i in range(start, len(my_string_arr)):
        path.append(my_string_arr[i])
        backtrack(i + 1, path)
        path.pop()

backtrack(0, path)
# this is printing from the global output above
print(output)
"""
output = 0
my_string = '0100010'
my_string_arr = list(my_string)
path = []
k = 5

# the entry point of the backtracking call is responsible returning output that's why we have the output increment when calling the backtrack calls
# it is also vital to return the output which is the 
def backtrack(start, path):
    output = 0
    if len(path) == k:
        # output += 1
        # return output
        # all I need is to return 1
        return 1
    for i in range(start, len(my_string_arr)):
        path.append(my_string_arr[i])
        output += backtrack(i + 1, path)
        path.pop()
    return output

print(backtrack(0, path))



