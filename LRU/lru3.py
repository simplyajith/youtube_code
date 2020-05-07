from collections import deque

class LRUCache:

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self,key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):

        if len(self.queue) == self.capacity:

            if key not in self.queue:
                x = self.queue.pop()
                if x in self.cache:
                    del self.cache[x]
            else:
                self.queue.remove(key)
        self.cache[key] = value
        if key in self.queue:
            self.queue.remove(key)
        self.queue.appendleft(key)



