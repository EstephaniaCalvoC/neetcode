"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]


Example 2:

Input: nums = [0,1,1]

Output: []


Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
"""

from typing import List
from collections import defaultdict


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    sorted_nums = sorted(nums)
    results = []

    for i, n in enumerate(sorted_nums):
        if i and n == sorted_nums[i - 1]:
            continue
        
        target = (n * -1) # n + (x + y) = 0
        
        # two pointers
        idx_l = i+1
        idx_r = len(nums) - 1

        while idx_l < idx_r:
            l = sorted_nums[idx_l]
            r = sorted_nums[idx_r]
            sum_pointers =  l + r 
            if sum_pointers == target:
                results.append([n, l, r])
                idx_l += 1
                while l == sorted_nums[idx_l] and idx_l < idx_r:
                    idx_l += 1
            if sum_pointers < target:
                idx_l += 1
            else:
                idx_r -= 1

    return results
        
if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(threeSum([0,0,0])) # [0,0,0]
    print(threeSum([0,1,1])) # [0,1,1]
    print(threeSum([0,0,0,0])) # [0,0,0]
