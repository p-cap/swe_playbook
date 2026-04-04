class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 1. Record the last index of every character
        last_occ = {c: i for i, c in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            # 2. If char is already used, we can't use it again
            if char in visited:
                continue
            
            # 3. Monotonic logic: 
            # If current char < top of stack AND top of stack appears later
            while stack and char < stack[-1] and i < last_occ[stack[-1]]:
                popped_char = stack.pop()
                visited.remove(popped_char)
            
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)

s = "cbacdcbc"
expected = "acdb"
my_solution = Solution()

result = my_solution.removeDuplicateLetters(s)
print(result)