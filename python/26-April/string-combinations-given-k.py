my_string = "010110"
my_string_arr = []

for letter in my_string:
    my_string_arr.append(letter)
k = 5

def _check_palindrome(temp_string):
    left = 0
    right = len(temp_string) - 1
    while left < right:
        if temp_string[left] != temp_string[right]:
            return 
        left += 1
        right -= 1
    return temp_string


def backtrack(start, temp_string):
    result = 0
    if len(temp_string) == k:
        palindrome_string = _check_palindrome(temp_string)
        if palindrome_string:
            print(''.join(palindrome_string))
            return 1
    for i in range(start,len(my_string_arr)):
       temp_string.append(my_string_arr[i])
       result += backtrack(i + 1, temp_string)
       temp_string.pop()
    return result

output = backtrack(0, [])
print(output)


