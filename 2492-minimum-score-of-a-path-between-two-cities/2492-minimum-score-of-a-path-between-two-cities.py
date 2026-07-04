from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        al = defaultdict(list)

        for u, v, c in roads:
            al[u].append((v, c))
            al[v].append((u, c))

        q = deque([1])
        visited = {1}
        ans = float("inf")

        while q:
            node = q.popleft()

            for nei, cost in al[node]:
                ans = min(ans, cost)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans
        