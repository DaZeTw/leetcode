class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]): continue
            target = nums[i]
            if (target>0): break
            start = i+1
            end = len(nums)-1
            while start<end:
                total = nums[start]+nums[end]+target
                if total>0:
                    end -=1
                elif total<0:
                    start +=1
                else:
                    ans.append([target,nums[start],nums[end]])
                    start +=1
                    while nums[start] == nums[start-1] and start<end:
                        start+=1
                
        return ans
                

            
        