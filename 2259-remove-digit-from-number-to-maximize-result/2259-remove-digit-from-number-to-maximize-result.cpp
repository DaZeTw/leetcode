class Solution {
public:
    string removeDigit(string number, char digit) {
        int last=-1;
        for(int i=0;i<number.length();i++)
        {
            char d=number[i];
            if(d==digit)
            {    last=i;
                 if(i+1<number.length() && number[i]<number[i+1])
                 break;
            }
           
            
            
        }
        return number.substr(0,last)+number.substr(last+1);
        
    }
};