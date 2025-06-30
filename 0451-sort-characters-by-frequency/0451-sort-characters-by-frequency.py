class Solution:
    def frequencySort(self, s: str) -> str:
        myDict = defaultdict(int)
        for ch in s:
            myDict[ch] = myDict.get(ch,0) + 1
        sortedDict = dict(sorted(myDict.items(), key = lambda item:item[1], reverse=True))
        res = ""
        for key,value in sortedDict.items():
            res += key*value
        return res