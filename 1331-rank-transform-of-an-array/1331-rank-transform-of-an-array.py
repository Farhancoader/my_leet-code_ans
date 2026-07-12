class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        h = {}
        t=0
        for i,num in enumerate(sorted(arr)):
            if num not in h:
                h[num]=i+1-t
            else:
                t+=1

        for i in range(len(arr)):
            arr[i]=h[arr[i]]
        return arr
        