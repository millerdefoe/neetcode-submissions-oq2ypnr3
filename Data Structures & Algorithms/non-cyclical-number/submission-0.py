class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n , self.sumOfSquares(n)
        
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
    
    def sumOfSquares(self, num):
        output = 0

        while num:
            digit = num % 10
            digit = digit ** 2
            output += digit
            num = num // 10
        return output
