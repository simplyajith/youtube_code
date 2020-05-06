class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency = []
        self.visited = False
        self.parent = None

class DFS:

    def dfs(self,startNode):

        startNode.visited = True
        stack =[]
        stack.append(startNode)

        while stack:
            curr_node = stack.pop()
            print(f"node: ", {curr_node.name})
            curr_adjlist = curr_node.adjacency

            for n in curr_adjlist:

                if not n.visited:
                    n.visited = True
                    stack.append(n)

class DFS_r:

    def dfs(self,startNode):

        startNode.visited = True
        print(f"node: ", {startNode.name})
        for n in reversed(startNode.adjacency):
            if not n.visited:
                n.visited = True
                self.dfs(n)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")


node1.adjacency.append(node2)
node1.adjacency.append(node3)
node2.adjacency.append(node4)
node4.adjacency.append(node5)
node3.adjacency.append(node6)



# " Output should be ABDEC"
df = DFS()
df.dfs(node1)
