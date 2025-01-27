#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        n = len(merged_array)
        median_index = n // 2

        if n % 2 == 0:
            median = (merged_array[median_index - 1] + merged_array[median_index]) / 2
        else:
            median = merged_array[median_index]
        return median

        
# @lc code=end

sol_class = Solution()
sol_class.findMedianSortedArrays([1,3],[2])

"""
The median index represents the position of the middle element(s) in the array. 
Subtracting 1 from it gives us the index of the previous element (to the left of the middle),
which is needed when the total number of elements is even.
"""