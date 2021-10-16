"""Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]"""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # create list of 0's the same length as nums
        ans = [0] * len(nums)
        
        # initialize counter variables for odds and evens
        odd = 1
        even = 0
        
        # loop through nums
        for num in nums:
            # if num is even add it to first index, then increment that counter by 2
            if num % 2 == 0:
                ans[even] = num
                even += 2 
            # if num is odd add it to second index, increment that counter by 2
            if num % 2 == 1:
                ans[odd] = num
                odd += 2

        # return updated list
        return ans