class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        temp = {}

        for num in nums:
            if num not in temp:
                left = temp.get(num-1,0)
                right = temp.get(num+1,0)
                curr = left+right+1

                temp[num] = curr
                ans = max(ans,curr)
                if left: temp[num-left]=curr
                if right: temp[num+right]=curr
        return ans