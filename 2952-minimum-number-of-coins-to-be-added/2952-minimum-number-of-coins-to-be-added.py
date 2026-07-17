class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        req = 0
        i=0
        reach = 0
        while reach<target:
            if i<len(coins) and coins[i]<=reach+1:
                reach+=coins[i]
                i+=1
            else:
                reach+=reach+1
                req+=1
        return req


        