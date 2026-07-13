class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []
        for length in range(len(str(low)),len(str(high))+1):
            for start in range(10-length):
                k = int(s[start:start+length])
                if k>high:
                    return ans
                if k<low:
                    continue
                ans.append(k)
        return ans