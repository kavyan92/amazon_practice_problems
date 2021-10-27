"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9"""

class Solution:
    def trap(self, height: List[int]) -> int:
        #keeps track of the total water as we traverse the elevation map
        #number of points on the map
        water = 0 
        n = len(height) 
        
        #lists to store the left_max and right_max of each point in the map
        left_max = [0]*n 
        right_max = [0]*n 

        #default values
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        #filling the left_max list
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])

        #filling the right_max list
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        #calculating the amount of water
        for i in range(n):
            water += min(left_max[i],right_max[i]) - height[i]

        return water

"""Runtime: 80 ms, faster than 63.62% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.5 MB, less than 97.25% of Python3 online submissions for Trapping Rain Water."""
