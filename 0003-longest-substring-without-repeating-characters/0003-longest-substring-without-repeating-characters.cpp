class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int>mp;
        int l{0},r{0};
        int ans{0};
        while (r<s.length()){
            mp[s[r]]++;
            while (mp[s[r]]>1){
                mp[s[l]]--;
                l++;
            }
            ans = max(ans,r-l+1);
            r++;
        }
        return ans;
    }
};