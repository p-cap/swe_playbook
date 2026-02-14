class Solution:
    def trap(self, height: List[int]) -> int:
        """
        approach
        - two pointer
        - we look for the max values from left to right
        - we look for the max values from right to left
        - the output will be the minimum between the two
        """

        ltr = []
        rtl = []
        output = 0
        test = []

        n = len(height)
        print(f'n: {n}')

        # sliding window
        # make sure I still understand sliding window

        # why was I haviing 'list out of range' error?
        # do I really understand sliding window

        # the sliding window for this example is 1
        # sliding window = n - len(window) + 1
        # sw = 5 - 2 + 1
        # sw = 4
        # sw = 5 - 2 + 1
        # count = 0
        # for i in range(sw):
        #     count += 1
        #     test.append(i)
        # print(f'sw: {count}')
        # print('==============')
        
        for i in range(1,n - 1):
            ltr.append(max(height[i], height[i - 1]))
        
        for i in range(n - 1, -1, -1):
            # this code is causing the IndexError
            print(f'i: {i}')
            # this indexError is at 11
            # when i = 11, we add 1, the height[12]
            # height[12] is causing the IndexError
            # whwn I changed from n - 1 to n - 2
            # it is not causing IndexError
            rtl.append(max(height[i], height[i + 1]))

        for i in range(n - 2):
            output += min(ltr[i], rtl[i])

        return output
    
    
IndexError: list index out of range
                              ~~~~~~^^^^^^^
    rtl.append(max(height[i], height[i + 1]))
Line 48 in trap (Solution.py)
    ret = Solution().trap(param_1)
Line 78 in _driver (Solution.py)
    ~~~~~~~^^
    _driver()
Line 93 in <module> (Solution.py)