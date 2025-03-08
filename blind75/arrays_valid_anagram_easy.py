# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # dict to keep track of chars we've seen
        seenS = {}
        seenT = {}

        for char in s:
            seenS[char] = char
        
        for char in t:
            seenT[char] = char

        if seenS == seenT:
            return True
        else:
            return False
        
        # can also just sort them and return
        # return sorted(s) == sorted(t)