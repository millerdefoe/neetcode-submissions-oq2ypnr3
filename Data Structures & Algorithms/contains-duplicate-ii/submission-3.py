class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashm = {}
        for i in range(len(nums)):
            if nums[i] not in hashm:
                hashm[nums[i]] = i
            else:
                if (abs(i-hashm[nums[i]])) <= k:
                    return True
                hashm[nums[i]] = i
                

        return False