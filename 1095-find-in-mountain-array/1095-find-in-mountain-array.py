# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mount: 'MountainArray') -> int:
        def bininc(l,r,target):
            while l<=r:
                mid = (l+r)//2
                k = mount.get(mid)
                if k==target:
                    return mid
                elif k>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        def bindec(l,r,target):
            while l<=r:
                mid = (l+r)//2
                k = mount.get(mid)
                if k==target:
                    return mid
                elif k>target:
                    l=mid+1
                else:
                    r=mid-1
            return -1

                

        l,r = 0,mount.length()-1
        index = -1
        peak = -1
        while l<r:
            mid = (l+r)//2
            if mount.get(mid)<mount.get(mid+1):
                l=mid+1
            else:
                r=mid
        peak = l
        left,right = bininc(0,peak,target),bindec(peak+1,mount.length()-1,target)
        if left==-1 and right==-1:
            return -1
        return left if left!=-1 else right


        