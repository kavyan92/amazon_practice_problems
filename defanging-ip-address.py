"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # initialize new empty string to keep track of defanged address
        defanged = ''
        #loop over each char in address
        for char in address:
            # if it is a '.', add '[.] to string, else, add char
            if char == '.':
                defanged = defanged + '[.]'
            else:
                defanged = defanged + char
        
        # return new string
        return defanged

