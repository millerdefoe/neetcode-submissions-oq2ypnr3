class Solution:

    def __init__(self, w: List[int]):
        self.weights = w  # raw weights, no need to normalize

    def pickIndex(self) -> int:
        return random.choices(range(len(self.weights)), weights=self.weights, k=1)[0]