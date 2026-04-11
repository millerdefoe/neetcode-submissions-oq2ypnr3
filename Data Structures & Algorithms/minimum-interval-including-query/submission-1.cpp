class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        vector<int> sortedQuery = queries;
        sort(sortedQuery.begin(), sortedQuery.end());
        sort(intervals.begin(), intervals.end());
        priority_queue<tuple<int,int>, vector<tuple<int,int>>, greater<tuple<int,int>>> minHeap;
        unordered_map<int,int> res = {};
        int i = 0;
        for (int q = 0; q < sortedQuery.size(); q++) {
            while (i < intervals.size() && intervals[i][0] <= sortedQuery[q]) {
                minHeap.push({intervals[i][1]-intervals[i][0]+1, intervals[i][1]});
                i++;
            }
            while (minHeap.size() > 0 && get<1>(minHeap.top()) < sortedQuery[q]) {
                minHeap.pop();
            }
            if (minHeap.empty()) {
                res[sortedQuery[q]] = -1;
            } else {
                res[sortedQuery[q]] = get<0>(minHeap.top());
            }
        }
        vector<int> answer;
        for (i = 0; i < queries.size(); i++) {
            answer.push_back(res[queries[i]]);
        }
        return answer;
    }
};
