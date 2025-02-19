class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            check[sorted_s].append(s)
        res = []
        for value in check.values():
            res.append(value)
        return res