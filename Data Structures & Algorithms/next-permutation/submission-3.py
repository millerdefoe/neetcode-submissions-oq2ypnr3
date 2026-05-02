class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #scan from right to left, find the first value that is strictly lesser than the next, flip it
        #if its in ascending order from right to left, reverse the whole list
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        print(f'{pivot=}')

        if pivot == -1:
            nums[:] = nums[::-1]
        else:
            target = 0
            for i in range(len(nums)-1, pivot, -1):
                if nums[pivot] < nums[i]:
                    target = i
                    break
            print(f'{target=}')
            nums[pivot], nums[target] = nums[target], nums[pivot]
            print(f'{nums=}')
            nums[pivot+1:] = nums[pivot+1:][::-1]


        return nums
            