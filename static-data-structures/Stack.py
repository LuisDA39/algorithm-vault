class Stack:
    def __init__(self, N):
        self.N = N
        self.top = 0
        self.stack = [0] * (N + 1)

    def push(self, value):
        if self.top == self.N:
            print("push() error: Stack is full")
            return
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == 0:
            print("pop() error: Stack is empty")
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    def is_empty(self):
        return self.top == 0

    def get_top(self):
        if self.top == 0:
            print("get_top() error: Stack is empty")
        else:
            return self.stack[self.top]


# Example
stack = Stack(5)

print("Is empty?", stack.is_empty())

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)  # Error

print("Top:", stack.get_top())
print("Is empty?", stack.is_empty())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Top:", stack.get_top())
print(stack.pop())
print(stack.pop())
stack.pop()  # Error

print("Is empty?", stack.is_empty())
