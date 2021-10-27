"""Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        ans = []
        for word in words:
            if not word:
                continue

            stack = [0]
            seen = {0}
            n = len(word)

            while stack:
                i = stack.pop()
                if i == n or (i > 0 and word[i:] in words):
                    ans.append(word)
                    break
                for x in range(n - i + 1):
                    if word[i: i + x] in words and i + x not in seen and x != n:
                        stack.append(i + x)
                        seen.add(i + x)
        return ans

"""Runtime: 1784 ms, faster than 95.10% of Python3 online submissions for Concatenated Words.
Memory Usage: 16.8 MB, less than 71.58% of Python3 online submissions for Concatenated Words."""