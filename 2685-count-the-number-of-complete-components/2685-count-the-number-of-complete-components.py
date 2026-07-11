from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        al = defaultdict(list)
        for u,v in edges:
            al[u].append(v)
            al[v].append(u)
        visited = [False]*n
        ans = 0
        def dfs(node):
            visited[node]=True
            vertices = 1
            degreesum = len(al[node])
            for nei in al[node]:
                if not visited[nei]:
                    v,d = dfs(nei)
                    vertices+=v
                    degreesum+=d
            return vertices,degreesum

        for node in range(n):
            if not visited[node]:
                v,d = dfs(node)
                if d  == v*(v-1):
                    ans+=1
        return ans

