class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
    #     ans = 0
    #     arr1_str = [str(x) for x in arr1]
    #     arr2_str = [str(x) for x in arr2]

    #     for s1 in arr1_str:
    #         for s2 in arr2_str:
    #             prefix_len = self.common_prefix_length(s1, s2)
    #             ans = max(ans, prefix_len)
    #     return ans

    # def common_prefix_length(self, s1: str, s2: str) -> int:
    #     n = min(len(s1), len(s2))
    #     for i in range(n):
    #         if s1[i] != s2[i]:
    #             return i
    #     return n
        prefix_map = set()

        for num in arr1:
            num = str(num)
            prefix = ""
            for ch in num:
                prefix += ch
                prefix_map.add(prefix)
        ans = 0
        for num in arr2:
            num = str(num)
            prefix = ""
            for ch in num:
                prefix += ch
                if(prefix in prefix_map):
                    ans = max(ans,len(prefix))
        return ans