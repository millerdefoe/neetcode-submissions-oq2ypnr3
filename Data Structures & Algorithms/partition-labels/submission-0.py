
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
             last[s[i]] = i
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
             end = max(end, last[s[i]])
             if i == end:
                  res.append(end-start +1)
                  start = end + 1
                  end = end + 1

        return res
             