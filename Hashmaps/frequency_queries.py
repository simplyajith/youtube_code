"""
You are given  queries. Each query is of the form two integers described below:
- 1 x : Insert x in your data structure.
- 2 y : Delete one occurence of y from your data structure, if present.
- 3 z: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
"""
class ListDict:

    def __init__(self):
        self.l = []
        self.dic = {}
        self.idx = 0

    def insert(self,val):
        self.l.append(val)
        self.dic[val] = self.dic.get(val,0) +1
        self.idx += 1

    def delete(self,val):
        if val in self.l:
            self.l.remove(val)
        self.dic[val] -=1

    def count_values(self,val_count):
        print(self.l)
        if val_count in self.dic.values():
            return 1
        else:
            return 0
x = ListDict()
x.insert(3)
x.delete(3)
print(x.count_values(2))
x.insert(4)
x.insert(5)
x.insert(5)
x.insert(4)
print(x.count_values(2))
print(x.dic)
x.delete(4)
print(x.l)
print(x.dic)


# def freqQuery(queries):
#     x = ListDict()
#     o = []
#     cmd, val = queries[0], queries[1]
#     print(cmd, val)
#     print(type(cmd[0]))
#     if cmd[0] == 1:
#         x.insert(val[0])
#     elif cmd[0] == 2:
#         x.delete(val[0])
#     elif cmd[0] == 3:
#         o.append(x.count_values(val[0]))
#     print(o)
#     return o






# q = int(input().strip())
#
# queries = []
#
# for _ in range(q):
#     queries.append(list(map(int, input().rstrip().split())))
#
# ans = freqQuery(queries)
# print(ans)



