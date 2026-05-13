class Solution:
    def climbStairs(self, n: int) -> int:
        """
        - base case
        - recursion relation 
        
        - The recursion relation is n = (n + 1) + (n + 2). Base case is when n is 1 it returns 1 and then n is 2 it returns 2. We are returnining the result of the recursion relation
        """
        dp = [0] * (n + 1)
        print(n)
        if n in dp:
            return dp[n]
        if n == 0: return 0
        if n == 1:  dp[n] = 1
        elif n == 2: dp[n] = 2
        else:
            dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
            return dp[n]
    
    
# never hits 0     
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        - base case
        - recursion relation 
        
        - The recursion relation is n = (n + 1) + (n + 2). Base case is when n is 1 it returns 1 and then n is 2 it returns 2. We are returnining the result of the recursion relation
        """
        dp = [0] * (n + 1)
        print(n)
        print(dp)
        if n in dp:
            return dp[n]
        # if n == 0: 
        #     print("hit me")
        #     return 0
        if n == 1:  dp[n] = 1
        elif n == 2: dp[n] = 2
        else:
            dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return dp[n]
    
"""
6
[0, 0, 0, 0, 0, 0, 0]
5
[0, 0, 0, 0, 0, 0]
4
[0, 0, 0, 0, 0]
3
[0, 0, 0, 0]
2
[0, 0, 0]
1
[0, 0]
2
[0, 0, 0]
3
[0, 0, 0, 0]
2
[0, 0, 0]
1
[0, 0]
4
[0, 0, 0, 0, 0]
3
[0, 0, 0, 0]
2
[0, 0, 0]
1
[0, 0]
2
[0, 0, 0]
"""

# I do not really understand DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n)
        dp[n-2] = 1 
        dp[n-1] = 2
        def recurse(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                dp[n] = dp[n-1] + dp[n-2]
            return dp[n]
        recurse(n)
        print(dp)
        return dp[n-1]
