# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        def bin_inc(l, r):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)

                if val == target:
                    return mid
                elif val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        def bin_dec(l, r):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)

                if val == target:
                    return mid
                elif val > target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        i = 1

        while i < n and mountainArr.get(i) > mountainArr.get(i - 1):
            i *= 2

        left = i // 2
        right = min(i, n - 1)

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        ans = bin_inc(0, peak)
        if ans != -1:
            return ans

        return bin_dec(peak + 1, n - 1)