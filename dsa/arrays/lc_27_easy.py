# 27. Remove Element
# Easy
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val in nums in place
        # return the number of elements in nums != to val

        #Input: nums = [0,1,2,2,3,0,4,2], val = 2
        # Output: 5, nums = [0,1,4,0,3,_,_,_]
        # k =5
        slow_ptr = 0

        for fast_ptr in range(0, len(nums)):
            if nums[fast_ptr] != val:
                nums[slow_ptr] = nums[fast_ptr]
                slow_ptr += 1
        return slow_ptr
        