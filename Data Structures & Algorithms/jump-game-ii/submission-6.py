
class Solution:
    def jump(self, nums: List[int]) -> int:
         nextMax = nums[0]
         if len(nums) == 1:
            return 0
         prevMax = 0
         tempMax = 0
         jumps = 0
         while True:
             for i in range(prevMax, min(nextMax + 1, len(nums))):
                  tempMax = max(tempMax, nums[i] + i)
             jumps += 1
             if nextMax >= (len(nums)-1):
                  return jumps

             if tempMax > nextMax:
                  prevMax = nextMax
                  nextMax = min(tempMax, len(nums)-1)
                  tempMax = 0
             
