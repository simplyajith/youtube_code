"""
Basics:
front, back
initially - front, back -1

enqueue(ele) - Add elements rear +1
dequeue - front moves to 1 position
front -
back
is empty

"""


class Queue:

    def __init__(self):
        self.queue = []
        self. front = -1
        self.back = -1

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, value):
        if self.is_empty():
            self.front += 1
            self.back += 1
        else:
            self.back += 1
        self.queue.append(value)
        return self.queue

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        elif self.front == self.back:
            self.front -= 1
            self.back -= 1
        else:
            self.back -= 1

        self.queue.pop(self.front)
        return self.queue

    def first(self):
        return self.queue[self.front]

    def last(self):
        return self.queue[self.back]


q = Queue()
print(q.is_empty())
print(q.enqueue("Aj"))
print(q.enqueue("PS"))
print(q.enqueue("BA"))
print(q.front)
print(q.back)
print(q.dequeue())
print(q.dequeue())
print(q.front)
print(q.back)
print(q.dequeue())
print(q.front)
print(q.back)
print(q.is_empty())
print(q.dequeue())
