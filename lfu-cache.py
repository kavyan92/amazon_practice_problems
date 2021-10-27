"""Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3"""

class LFUCache:

    def __init__(self, capacity: int):
        self.__capa = capacity
        self.__size = 0
        self.__min_freq = float("inf")
        self.__freq_to_nodes = collections.defaultdict(collections.OrderedDict)
        self.__key_to_freq = {}

    def get(self, key: int) -> int:
        if key not in self.__key_to_freq:
            return -1
        value = self.__freq_to_nodes[self.__key_to_freq[key]][key]
        self.__update(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.__capa <= 0:
            return

        if key not in self.__key_to_freq and self.__size == self.__capa:
            del self.__key_to_freq[self.__freq_to_nodes[self.__min_freq].popitem(last=False)[0]]
            if not self.__freq_to_nodes[self.__min_freq]:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(key, value)
        
    def __update(self, key, value):
        freq = 0
        if key in self.__key_to_freq:
            freq = self.__key_to_freq[key]
            del self.__freq_to_nodes[freq][key]
            if not self.__freq_to_nodes[freq]:
                del self.__freq_to_nodes[freq]
                if self.__min_freq == freq:
                    self.__min_freq += 1
            self.__size -= 1

        freq += 1
        self.__min_freq = min(self.__min_freq, freq)
        self.__key_to_freq[key] = freq
        self.__freq_to_nodes[freq][key] = value
        self.__size += 1


"""Runtime: 900 ms, faster than 76.05% of Python3 online submissions for LFU Cache.
Memory Usage: 77.9 MB, less than 25.55% of Python3 online submissions for LFU Cache."""