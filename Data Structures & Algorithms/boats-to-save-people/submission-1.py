class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        boat = 0
        while i <= j:
            if people[j] == limit:
                boat += 1
                j -= 1
            elif people[i] + people[j] == limit:
                boat += 1
                j -= 1
                i += 1
            elif people[i] + people[j] > limit:
                boat += 1
                j -= 1
            else:
                boat += 1
                j -= 1
                i += 1
        return boat