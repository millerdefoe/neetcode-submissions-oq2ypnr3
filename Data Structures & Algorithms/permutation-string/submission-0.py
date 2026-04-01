class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import defaultdict
        
        s1map = defaultdict(int)
        s2map = defaultdict(int)
        
        # Build frequency maps
        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1
        
        # Initial matches - check ALL characters that appear in either map
        def count_matches():
            matches = 0
            all_chars = set(s1map.keys()) | set(s2map.keys())
            for char in all_chars:
                if s1map[char] == s2map[char]:
                    matches += 1
            return matches
        
        matches = count_matches()
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s1map == s2map:  # Simpler check: direct comparison
                return True
                
            # Add right character
            right_char = s2[r]
            if s1map[right_char] == s2map[right_char]:
                matches -= 1
            s2map[right_char] += 1
            if s1map[right_char] == s2map[right_char]:
                matches += 1
                
            # Remove left character  
            left_char = s2[l]
            if s1map[left_char] == s2map[left_char]:
                matches -= 1
            s2map[left_char] -= 1
            if s1map[left_char] == s2map[left_char]:
                matches += 1
                
            l += 1
        
        return s1map == s2map