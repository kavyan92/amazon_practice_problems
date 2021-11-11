"""Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[int(n-1):int(n)]
            if n < 100:
                return [tens[int(n/10-2)]] + words(n%10)
            if n < 1000:
                return [to19[int(n/100-1)]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

"""Runtime: 28 ms, faster than 92.69% of Python3 online submissions for Integer to English Words.
Memory Usage: 14.5 MB, less than 26.10% of Python3 online submissions for Integer to English Words."""