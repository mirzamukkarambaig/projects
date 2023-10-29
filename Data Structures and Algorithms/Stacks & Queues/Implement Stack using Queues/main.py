class MyStack:

    def __init__(self):
        self.stack = []
        self.top_index = -1  

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_index += 1

    def pop(self) -> int:
        if self.top_index == -1:
            raise Exception("Stack is empty!")
        self.top_index -= 1
        return self.stack.pop()
        
    def top(self) -> int:  
        if self.top_index == -1:
            raise Exception("Stack is empty!")
        return self.stack[self.top_index]

    def empty(self) -> bool:
        return len(self.stack) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()