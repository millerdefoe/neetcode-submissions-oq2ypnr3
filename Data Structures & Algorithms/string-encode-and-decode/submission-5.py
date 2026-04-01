class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            if len(i) == 0:
                res += ("%")
            for j, char in enumerate(i):
                res += str(ord(char))
                res += ("/")
                if j == len(i) - 1:

                    res += ("%")
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        count = 0
        store = ""
        word = ""
        for i in s:
            if i == "%":
                res.append(word)
                word = ""
                count += 1
            elif i == "/":
                word += (chr(int(store)))
                store = ""
            else:
                store += i
        return res
            
