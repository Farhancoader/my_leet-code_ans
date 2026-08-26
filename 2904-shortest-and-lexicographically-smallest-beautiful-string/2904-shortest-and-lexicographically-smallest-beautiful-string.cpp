class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int left = 0;
        int n = s.size();
        int start=0,end=INT_MAX;
        int curr = 0;
        for(int right = 0; right<n; right++){

            if(s[right] == '1') curr++;
            if(curr == k){
                while (s[left] == '0') {
                    left++;
                }
                if((right - left  < end - start) || (right - left == end - start && string_view(s.data() + left, right - left + 1) < string_view(s.data() + start, end - start + 1)) ){
                    start = left ; end = right;
                }
                curr--;left++;
                    while(left<n && s[left]!='1'){
                        left++;
                    }
            }
        }
        if(end==INT_MAX)return "";
        return string(string_view(s.begin()+start,s.begin()+end+1));
    }
};