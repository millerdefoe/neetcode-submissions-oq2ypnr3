class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(i, curString):
            if i >= len(digits):
                if curString:
                    res.append("".join(curString.copy()))
                return 

            for d in digitToChar[digits[i]]:  
                curString.append(d)
                dfs(i+1, curString)
                curString.pop()

            #curString.append(digitToChar[digits[i]][1])
            #dfs(i+1, curString)
            #curString.pop()
        
            #curString.append(digitToChar[digits[i]][2])
            #dfs(i+1, curString)
            #curString.pop()

        dfs(0, [])

        return res
