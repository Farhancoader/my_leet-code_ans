class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos,spe] for pos,spe in zip(position,speed)]
        pairs = sorted(pairs,reverse=True)
        stack = []
        for pos,spe in pairs:
            if len(stack)>=1 and (target-pos)/spe<=stack[-1]:
                continue
            else:
                stack.append((target-pos)/spe)
        return len(stack)