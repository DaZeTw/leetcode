class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf, ans = 1, 1, [1]*n
        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
            ans[n-1-i] *= suf
            suf *= nums[n-1-i]
        return ans 