class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int del = 0;
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b) {
            return a[1] < b[1];
        });
        vector<int> prev = intervals[0];
        for (int i = 1; i < intervals.size(); i++) {
            if (prev[1] <= intervals[i][0]) {
                prev = intervals[i];
            } else {
                del++;
            }
        }
        return del;
    }
};
