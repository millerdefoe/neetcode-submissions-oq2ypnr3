class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snum = sorted(nums)
        res = []
        for i,a in enumerate(snum):
            if i > 0 and snum[i-1] == a:
                continue
            l,r = i+1, len(snum) - 1
            while l<r:
                threeSum = a + snum[l] + snum[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,snum[l],snum[r]])
                    l += 1
                    while snum[l] == snum[l-1] and l < r:
                        l += 1
        return res