class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1, -1, -1):
            if (numbers[i] + numbers[0] > target):
                print(numbers[i] - target)
                continue
            for j in range(i):
                if numbers[i] + numbers[j] == target:
                    return [j+1,i+1]
        return False
            