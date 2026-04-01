class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = defaultdict(list)
        for string in strs:
            sortedS = ''.join(sorted(string))
            hashm[sortedS].append(string)
        return list(hashm.values())

