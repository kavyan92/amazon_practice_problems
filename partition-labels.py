"""You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create list to store results and a dictionary to keep track of all letters
        answer = []
        letters = {}
        # loop through string and add letters to dict
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        # create a set to keep track of letters that we've seen as we loop through
        seen = set()
        # loop through string again and add each new char to set
        for idx, char in enumerate(s):
            seen.add(char)
            # if there is still a value for the letter in the dict, subtract 1
            if letters[char] > 1:  
                letters[char] -= 1  
            # else if it is one, subtract one to make it zero
            else:
                # check dict to see if previously seen letter are all zero
                letters[char] -= 1    
                for ch in seen: 
                    potential_string = True  
                    # if any are not zero, break and return to looping
                    if letters[ch] != 0:  
                        potential_string = False
                        break
                # if all are zero, use idx to find the length of this substring and append to results list
                if potential_string is True:     
                    sub_string_length = idx + 1 - sum(answer)
                    answer.append(sub_string_length)

        # return answer
        return answer

"""Runtime: 36 ms, faster than 91.17% of Python3 online submissions for Partition Labels.
Memory Usage: 14.3 MB, less than 54.92% of Python3 online submissions for Partition Labels."""