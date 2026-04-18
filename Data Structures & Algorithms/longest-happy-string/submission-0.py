class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        longest = 0

        maxHeap = [(-a,'a'),(-b,'b'),(-c,'c')]
        heapq.heapify(maxHeap)
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            if count < 0:
                if len(res) <= 1 or not (res[-1] == res[-2] == letter):
                    res.append(letter)
                    heapq.heappush(maxHeap, (count+1, letter))
                else:
                    if not maxHeap:
                        break
                    count2, letter2 = heapq.heappop(maxHeap)
                    if count2 < 0:
                        res.append(letter2)
                        heapq.heappush(maxHeap, (count2+1, letter2))
                        heapq.heappush(maxHeap, (count, letter))    

        return "".join(res)
        