class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        cPointer = 0 #compression pointer where i write to
        counter = 1
        for i in range(1,len(chars)):
            if chars[i-1] == chars[i]:
                counter += 1

            else:
                chars[cPointer] = chars[i-1]
                cPointer += 1
                if counter > 1:
                    stringC = str(counter)
                    for c in stringC:
                        chars[cPointer] = c
                        cPointer += 1
                counter = 1
        
        chars[cPointer] = chars[len(chars)-1]
        cPointer += 1
        if counter > 1:
            stringC = str(counter)
            for c in stringC:
                chars[cPointer] = c
                cPointer += 1


        return cPointer