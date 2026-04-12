class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int ROWS = matrix.size(), COLS = matrix[0].size();
        for (int r = 0; r < ROWS; r++) {
            for (int c = r+1; c < COLS; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        }
        for (int r = 0; r < ROWS; r++) {
            reverse(matrix[r].begin(), matrix[r].end());
        }
    }
};
