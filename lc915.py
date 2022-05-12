# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
#     Every element in left is less than or equal to every element in right.
#     left and right are non-empty.
#     left has the smallest possible size.
# Return the length of left after such a partitioning.
# Test cases are generated such that partitioning exists.
class Solution(object):
    def partitionDisjoint(self, nums):
        right_min = min(nums[1:])
        left_max = nums[0]
        for i, num in enumerate(nums[1:], start=1):
            if left_max <= right_min:
                return i
            if num > left_max:
                left_max = num
            elif num == right_min:
                right_min = min(nums[i+1:])
