# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True # duplicate found
            seen[num] = True # add num to seen dict.
        return False # no duplicates found


        
         