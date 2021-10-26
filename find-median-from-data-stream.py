"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0"""

class MedianFinder:

    def __init__(self):
        import heapq
        
        self.count = 0
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.count % 2  == 0:
            if len(self.minHeap) == 0:
                heapq.heappush(self.minHeap, num)
            else:
                if num <= -self.maxHeap[0]:
                    heapq.heappush(self.maxHeap, -num)
                    heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                else:
                    heapq.heappush(self.minHeap, num)
        else:
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.maxHeap, -num)
            
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (float(self.minHeap[0]) + float(-self.maxHeap[0])) / 2.0
        else:
            return float(self.minHeap[0])
        