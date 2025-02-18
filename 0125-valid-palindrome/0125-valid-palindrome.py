class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        # new_s=''.join(c for c in s if c.isalpha())
        new_s=''.join(c for c in s if c.isalnum())
        new_s=new_s.lower()
        # print(new_s)
        # n = len(new_s)
        # for i in range(0,n//2):
        #     print(i)
        #     if (new_s[i]!=new_s[n-i-1]): return False
        # return True
        if(new_s==new_s[::-1]): 
            return True
        else:
            return False

        

        