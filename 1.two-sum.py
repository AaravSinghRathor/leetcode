#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements_till_now = {}
        for index, num in enumerate(nums):
            if (target-num) in elements_till_now:
                return (elements_till_now[target-num], index)
            elements_till_now[num] = index
        return
# @lc code=end

