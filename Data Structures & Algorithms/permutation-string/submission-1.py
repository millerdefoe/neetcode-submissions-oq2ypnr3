class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import defaultdict
        
        s1map = defaultdict(int)
        s2map = defaultdict(int)
        
        # Build initial window
        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1
        
        # Check initial window
        if s1map == s2map:
            return True
        
        # Sliding window - no matches variable needed!
        l = 0
        for r in range(len(s1), len(s2)):
            # Add right character
            s2map[s2[r]] += 1
            
            # Remove left character
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]  # Clean up zeros
            
            # Check if current window matches
            if s1map == s2map:
                return True
            
            l += 1
        
        return False