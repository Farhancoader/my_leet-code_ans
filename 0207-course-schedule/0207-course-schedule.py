class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}

        for cre, pre in prerequisites:
            d[cre].append(pre)

        v = set()
        def dfs(cres):
            if cres in v:
                return False
            if d[cres] ==[]:
                return True
            
            v.add(cres)

            for pre in d[cres]:
                if not dfs(pre):
                    return False
                
            v.remove(cres)
            d[cres] = []
            return True
        
        for cres in range(numCourses):
            if not dfs(cres):
                return False
        
        return True
        