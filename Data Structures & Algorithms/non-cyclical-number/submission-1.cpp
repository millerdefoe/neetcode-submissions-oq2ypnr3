class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = sumOfSquares(n);
        while (slow != fast) {
            fast = sumOfSquares(fast);
            fast = sumOfSquares(fast);
            slow = sumOfSquares(slow);
        }
        return fast == 1;
    }


private:
    int sumOfSquares(int num) {
        int output = 0;
        int digit = 0;
        while (num) {
            digit = num % 10;
            digit = digit * digit;
            output += digit;
            num /= 10;
        }
        return output;
    }
};