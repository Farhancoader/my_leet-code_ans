from collections import Counter
class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.grp = {}
        self.maxcnt = 0

    def push(self, val: int) -> None:
        valcnt = 1+self.cnt.get(val,0)
        self.cnt[val] = valcnt
        if valcnt>self.maxcnt:
            self.maxcnt = valcnt
            self.grp[valcnt]=[]
        self.grp[valcnt].append(val)

    def pop(self) -> int:
        if self.maxcnt==0:
            return -1
        ans = self.grp[self.maxcnt].pop()
        self.cnt[ans]-=1
        if not self.grp[self.maxcnt]:
            self.maxcnt-=1
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()