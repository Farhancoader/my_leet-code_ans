class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in  self.d:
            return ""
        l,r = 0,len(self.d[key])-1
        pos = ""
        while l<=r:
            mid = (l+r)//2
            time,value = self.d[key][mid]
            if time==timestamp:
                return value
            elif time<timestamp:
                pos = value
                l=mid+1
            else:
                r=mid-1
        return pos
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)