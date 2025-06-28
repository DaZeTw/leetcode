class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        countMap = defaultdict(int)
        res = []
        for num in nums:
            if num not in countMap:
                countMap[num] = 1
            else:
                res.append(num)
        return res