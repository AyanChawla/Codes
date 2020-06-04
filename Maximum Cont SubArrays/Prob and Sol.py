# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
# This is kadane algorithm for negative numbers.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            curr += nums[i]
            if curr < nums[i]:
                curr = nums[i]
            if curr > mx:
                mx = curr
        return mx
        
