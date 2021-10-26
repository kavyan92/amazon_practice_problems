"""You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example 3:
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example 4:
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # initialize variables to iterate through each list
        x = 0
        y = 0
        # create list to store results
        ans = []
        
        # while the variables are less than the length of lists, keep looping
        while x < len(firstList) and y < len(secondList):
            # find the max of the first item of the first interval in each list
            mx = max(firstList[x][0], secondList[y][0])
            # find the min of the second item of the second list
            mn = min(firstList[x][1], secondList[y][1])
            # if max is less than min, this is your first interval
            if mx <= mn:
                # add to result list
                ans.append([mx, mn])
            # if the second item of the first item of first list is less than the second item of the second list, increment first counter by one, continue looping
            if firstList[x][1] < secondList[y][1]:
                x += 1
            # after that comparison, increment the second counter by 1 and continue looping
            else:
                y += 1
        # return result list
        return ans

        