"""
Basics:
1) push - increment top by 1, assign value to top.
2) pop - decrement top by 1.
3) top - return value of top.
"""

# Initialize an array
stack = []

# initialize top variable as -1
top = -1

# push function for stack
# def push(value):
#     top +=1
#     stack[top] = value
class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,value):
        self.top += 1
        self.stack.append(value)

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return stack
        self.top -=1
        self.stack.pop()
        return stack

    def peek(self):
        return self.stack[self.top]

    def print_stack(self):
        print(f"Printing the stack with top ,{self.top}")
        for i in range(self.top,-1,-1):
            if i == self.top:
                print(self.stack[i], " <----- Top")
            else:
                print(self.stack[i])
            print("|")

s = Stack()
s.push(8)
s.push(9)
s.push(10)
# s.print_stack()
s.pop()
#
s.push(11)
s.print_stack()

v = Stack()
v.push(5)
v.push(66)
v.push(12)
# s.print_stack()
v.pop()

v.push(778)
print(v.peek())
v.print_stack()

