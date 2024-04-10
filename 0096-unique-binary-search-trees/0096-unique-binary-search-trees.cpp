class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1,0);
        dp[0] = dp[1] =1;
        for (int i=2;i<=n;i++){
            for (int j=0;j<i;j++){
                dp[i] += dp[j]*dp[i-j-1];
            }
        }
        return dp[n];
    }
};

/*
Time: O(n^2)
Space: O(n)
1. Prepare
- vector DP to store all the state of trees 
2. Work
- Consider all the nodes like as roots
- Each root have left side and right side, so there are how many ways to define all circumstances of one root?
- It will be equal to DP[left]*DP[right]
- For number n, it has n ways to choose roots, so the result with each n is n*DP[left]*DP[right]
*/ 