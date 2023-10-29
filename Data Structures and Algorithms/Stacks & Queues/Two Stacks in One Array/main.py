class TwoStacks:
    def __init__(self, size):
        self.array = [None] * size
        self.top1 = 0
        self.top2 = size - 1

    def push1(self, value):
        if self.top1 <= self.top2:
            self.array[self.top1] = value
            self.top1 += 1
        else:
            raise Exception("Stack1 Overflow!")

    def push2(self, value):
        if self.top2 >= self.top1:
            self.array[self.top2] = value
            self.top2 -= 1
        else:
            raise Exception("Stack2 Overflow!")

    def pop1(self):
        if self.top1 > 0:  
            self.top1 -= 1
            value = self.array[self.top1]
            self.array[self.top1] = None
            return value
        else:
            raise Exception("Stack1 Underflow!")

    def pop2(self):
        if self.top2 < len(self.array) - 1:  
            self.top2 += 1
            value = self.array[self.top2]
            self.array[self.top2] = None
            return value
        else:
            raise Exception("Stack2 Underflow!")

    def print(self) -> None:
        print(self.array)