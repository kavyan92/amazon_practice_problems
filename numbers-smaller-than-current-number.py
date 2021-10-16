"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # create empty list to keep track of results
        ans = []
        # initialize counter variable to keep track of nums that are smaller
        count = 0
        
        # loop over each num in list
        for num in nums:
            # assign new var to current num
            temp = num
            # loop over list again and if any numbers are less than temp, increment counter
            for rest in nums: 
                if rest < temp:
                    count += 1
            # add counter to new list
            ans.append(count)
            # reset counter
            count = 0
            
        # return new list
        return ans