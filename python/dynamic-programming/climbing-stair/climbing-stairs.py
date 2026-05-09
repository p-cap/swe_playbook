# this solution will timeout
class Solution:
    def climbStairsRecurse(self, n: int) -> int:
        output = 0
        def recurse(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return recurse(n - 1) + recurse(n - 2)
        output = recurse(n)
        return output

class Solution:
    def climbStairs(self, n: int) -> int:
        # this never gets to the memo list
        if n <= 2: return n

        memo = [0] * (n + 1)

        def recurse(i):
            if i <= 2: return i
            if memo[i] != 0: return memo[i]

            memo[i] = recurse(i-1) + recurse(i-2)
            return memo[i]

        recurse(n)
        print(memo)
        return memo[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        # this never gets to the memo list
        memo = [0] * (n + 1)
        def recurse(i):
            if i <= 2: memo[i] = i
            if memo[i] != 0: return memo[i]

            memo[i] = recurse(i-1) + recurse(i-2)
            return memo[i]

        recurse(n)
        print(memo)
        return memo[n]
