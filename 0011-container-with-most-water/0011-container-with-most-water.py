class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n-1
        ans = 0
        while start<=end:
            volume = min(height[start],height[end])*(end-start)
            ans = max(ans,volume)
            if (height[start]<height[end]):
                start +=1
            else:
                end -=1
        return ans
        