"""Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # create two sets to keep track of nums as we loop through the list
        once = set()
        twice = set()
        # loop through each item in nums
        for num in nums:
            # if its already in set(once), add it to set(twice)
            if num in once:
                twice.add(num)
            # else add it to set(once)
            else:
                once.add(num)
        
        # return set(twice)
        return twice

"""Runtime: 344 ms, faster than 85.51% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 24.2 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array."""