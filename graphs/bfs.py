class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency = []
        self.visited = False
        self.parent = None

class BreadthFirstSearch:

    def bfs(self,startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            currentNode = queue.pop(0)
            adj = currentNode.adjacency
            print(f"{currentNode.name}")

            for n in adj:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.adjacency.append(node2)
node2.adjacency.append(node3)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
