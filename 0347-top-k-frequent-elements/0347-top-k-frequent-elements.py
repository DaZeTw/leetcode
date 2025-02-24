class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        count_map={}
        result = []
        for num in nums:
            if num not in count_map:
                count_map[num]=1
            else:
                count_map[num]+=1
        for key,value in count_map.items():
            heapq.heappush(pq,(value,key))
            if (len(pq)>k): heapq.heappop(pq)
        for i in range(0,k):
            pair = heapq.heappop(pq)
            result.append(pair[1])
        return result

# Input: list of int (not sorted) and integer k (1<=k<=len(nums))
# Output: list of in and in any order 
