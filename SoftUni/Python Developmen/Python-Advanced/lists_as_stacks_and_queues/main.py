class Stack:
    def __init__(self):
        self.internal_values = []

    def push(self, values):
        return self.internal_values.append(values)

    def pop(self):
        return self.internal_values.pop()

    def peek(self):
        return self.internal_values[-1]

    @property
    def is_empy(self):
        return len(self.internal_values) == 0


s = Stack()

[s.push(x) for x in range(5)]

while not s.is_empy():
    print(s.pop())
