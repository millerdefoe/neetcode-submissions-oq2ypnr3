class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #find intersection, return first valid intersection, else return []
        slots1.sort(key = lambda x:x[0])
        slots2.sort(key = lambda x:x[0])
        for s1 in slots1:
            for s2 in slots2:
                if s1[1] > s2[0] and s1[0] < s2[1]:
                    intersect = [max(s1[0],s2[0]), min(s1[1],s2[1])]
                    if intersect[1] - intersect[0] >= duration:
                        return [intersect[0], intersect[0] + duration]
                elif s2[1] > s1[0] and s2[0] < s1[1]:
                    intersect = [max(s1[0],s2[0]), min(s1[1],s2[1])]
                    if intersect[1] - intersect[0] >= duration:
                        return [intersect[0], intersect[0] + duration]
            
        return []
