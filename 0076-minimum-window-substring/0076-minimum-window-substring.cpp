class Solution {
public:
    string minWindow(string s, string t) {
    unordered_map<char, int> mp;
    for (char c : t) mp[c]++;

    int start = 0, end = 0, counter = mp.size();
    int minLen = INT_MAX, minStart = 0;

    while (end < s.size()) {
        char c1 = s[end];
        if (mp.find(c1) != mp.end()) {
            mp[c1]--;
            if (mp[c1] == 0) counter--;
        }
        end++;
        while (counter == 0) {
            if (end - start < minLen) {
                minLen = end - start;
                minStart = start;
            }
            char c2 = s[start];
            if (mp.find(c2) != mp.end()) {
                mp[c2]++;
                if (mp[c2] > 0) counter++;
            }
            start++;
        }
    }

    return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
}
};
