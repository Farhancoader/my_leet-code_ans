class Solution:
    def makesquare(self, matchs: List[int]) -> bool:
        length = sum(matchs)//4
        sides = [0]*4
        if sum(matchs)/4!=length:
            return False
        matchs.sort(reverse=True)
        def dfs(i):
            if i==len(matchs):
                return True
            for j in range(4):
                if sides[j]+matchs[i]<=length:
                    sides[j]+=matchs[i]
                    if dfs(i+1):
                        return True
                    sides[j]-=matchs[i]
            return False
        return dfs(0)

            
        