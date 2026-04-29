class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #find intersection, return first valid intersection, else return []
        slots1.sort(key = lambda x:x[0])
        slots2.sort(key = lambda x:x[0])
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            s1 = slots1[i]
            s2 = slots2[j]
            intersect = [max(s1[0],s2[0]), min(s1[1],s2[1])]
            if intersect[1] - intersect[0] >= duration:
                return [intersect[0], intersect[0] + duration]
            
            if s1[1] > s2[1]:
                j += 1
            else:
                i += 1
            
        return []
