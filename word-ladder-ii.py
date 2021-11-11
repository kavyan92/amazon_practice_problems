"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence."""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        ans = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    ans.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for char in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + char + word[i+1:]
                            if new_word in wordset:
                                newlayer[new_word] += [j+[new_word] for j in layer[word]]
            wordset -= set(newlayer.keys())
            layer = newlayer
            
        return ans

"""Runtime: 52 ms, faster than 75.55% of Python3 online submissions for Word Ladder II.
Memory Usage: 14.9 MB, less than 36.47% of Python3 online submissions for Word Ladder II."""