class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        runningTrip = [0,0,0]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            else:
                runningTrip[0] = max(runningTrip[0], triplet[0])
                runningTrip[1] = max(runningTrip[1], triplet[1])
                runningTrip[2] = max(runningTrip[2], triplet[2])
        return runningTrip == target