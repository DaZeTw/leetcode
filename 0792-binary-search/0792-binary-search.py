class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            print(mid)
            if (nums[mid]==target): return mid
            if (nums[mid]<target):
                start = mid + 1
                print("Start:",start)
            else:
                end = mid - 1
                print("End:",end)
        return -1 
        