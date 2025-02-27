class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        mid = 0
        while start<=end:
            mid = (start+end)//2
            value = nums[mid]
            print(value)
            if (value > nums[end] and value>=nums[start]):
                start = mid+1
            elif (value<nums[end] and value<nums[start]):
                end = mid
            else:
                end = mid - 1
        return nums[mid]