class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        unordered_map<int,int> mp;
        int l{0}, r{0};
        int ans = INT_MAX;  
        while (r < cards.size()){
            mp[cards[r]]++;
            if (mp[cards[r]] > 1) {
                while (cards[r] != cards[l]) {
                    mp[cards[l]]--; 
                    l++;
                }
                ans = min(ans, r-l+1);
                // Correcting: skip the current repeating number
                mp[cards[l]]--; 
                l++; 
            }
            r++;
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
