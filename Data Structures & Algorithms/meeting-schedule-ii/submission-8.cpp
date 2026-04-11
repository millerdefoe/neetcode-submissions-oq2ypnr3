/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.empty()) return 0;
        priority_queue<int, vector<int>, greater<int>> minHeap;
        sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b){
            return a.start < b.start;
        });
        minHeap.push(intervals[0].end);

        for (int i = 1; i < intervals.size(); i++) {
            if (minHeap.top() <= intervals[i].start) {
                minHeap.pop();
                minHeap.push(intervals[i].end);
            } else {
                minHeap.push(intervals[i].end);
            }
        }
        return minHeap.size();

    }
};
