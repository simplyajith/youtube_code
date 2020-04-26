class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end = " ")
            temp = temp.next

def delete_node(head, node):

    current = head
    if current.value == node:
        head = None
        current = current.next
        print(current.value)
        head = current
        print(head.value)
    else:

        while current.next is not None:
            if current.next.value == node:
                previous = current
                current = previous.next
                previous.next = current.next
                current = None
                return head
            current = current.next

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Nodes in linked list are: ",end = "" )
    print(head.print_list())
    result = delete_node(head,5)
    print("Nodes in linked list are: ", end="")
    print(result.print_list())

main()



