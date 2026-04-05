class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq = Counter(hand)

        for v in sorted(freq):
            if freq[v] > 0:
                count = freq[v]
                for i in range(groupSize):
                    freq[v] -= count
                    if freq[v] < 0:
                        return False
                    v += 1
        return True

