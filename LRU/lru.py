import math
import time

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.d:
            # self.lru[key] = self.lru.get(key,0) + 1
            if key in self.queue:
                self.queue.pop(self.queue.index(key))
            self.queue.append(key)
            return self.d[key]


        else:
            return -1

    # def get_lru(self):
    #     mini = math.inf
    #     mini_key = None
    #     if self.lru:
    #         for key, value in self.lru.items():
    #             if value < mini:
    #                 mini = value
    #                 mini_key = key
    #     return mini_key

    def put(self, key: int, value: int) -> None:
        if len(self.queue) == self.capacity:
            if key not in self.queue:
                least_recent_used = self.queue.pop(0)
                del self.d[least_recent_used]
            # del self.lru[least_used]
        self.d[key] = value
        if key in self.queue:
            self.queue.pop(self.queue.index(key))
        self.queue.append(key)



l = LRUCache(2)
l.get(2)
l.put(2,6)
print(l.d)
l.get(1)
l.put(1,5)
print(l.d)
l.put(1,2)
l.get(1)
l.get(2)

print(l.queue)
print(l.d)
