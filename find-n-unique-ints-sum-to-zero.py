"""Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # create empty set to stores results
        ans = set()
        
        # if n is even, add positive and negative values of n//2 and then decrement by 2 each time until n = 0
        if n % 2 == 0:
            while n > 0:
                ans.add(n//2)
                ans.add(-(n//2))
                n -= 2
        # if  n is odd, first add zero, decrement by 1 and then add n//2 until n = 0, and decrement by 2
        else:
            ans.add(0)
            n -= 1
            while n > 0:
                ans.add(n//2)
                ans.add(-(n//2))
                n -= 2
        
        # return resulting set
        return ans

"""Runtime: 32 ms, faster than 86.12% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 14.4 MB, less than 14.46% of Python3 online submissions for Find N Unique Integers Sum up to Zero."""