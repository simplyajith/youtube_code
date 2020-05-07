# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFS:

    def bfs(self, root):
        result = []
        parent = {}
        queue = [root]
        while queue:
            current_level = []
            level_size = len(queue)

            for _ in range(level_size):
                current_node = queue.pop(0)
                current_level.append(current_node.val)
                parent[current_node.val] = []

                if current_node.left:
                    queue.append(current_node.left)
                    parent[current_node.val] = [current_node.left.val]

                if current_node.right:
                    queue.append(current_node.right)
                    parent[current_node.val].append(current_node.right.val)

            print(current_level)

            result.append(current_level)
        print(result,parent)
        return result, parent

    def isCousins(self, root, x, y):
        r,p = self.bfs(root)
        level = False
        cousins = False
        for i in r:
            if x in i and y in i:
                level = True
        if not level:
            return False
        else:
            for v in p.values():
                print(v)
                if x in v and y in v:
                    cousins = False
                    return False
            else:
                cousins = True

        return cousins

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.left = node2
node1.right = node3
node2.left = node4

b =BFS()
b.bfs(node1)
print(b.isCousins(node1,2,3))