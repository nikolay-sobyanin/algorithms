class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        print(len(self.stack))

    def push(self, n: int):
        self.stack.append(n)
        print('ok')

    def pop(self):
        if len(self.stack) == 0:
            print('error')
            return
        print(self.stack.pop())

    def back(self):
        if len(self.stack) == 0:
            print('error')
            return
        print(self.stack[-1])

    def clear(self):
        self.stack.clear()
        print('ok')

    @staticmethod
    def exit():
        print('bye')


def handler():
    stack = Stack()
    flag = True
    while flag:
        s = input().strip().split()
        cmd = s[0]
        if cmd == 'push':
            n = int(s[1])
            stack.push(n)
        elif cmd == 'pop':
            stack.pop()
        elif cmd == 'back':
            stack.back()
        elif cmd == 'size':
            stack.size()
        elif cmd == 'clear':
            stack.clear()
        elif cmd == 'exit':
            stack.exit()
            flag = False


handler()
