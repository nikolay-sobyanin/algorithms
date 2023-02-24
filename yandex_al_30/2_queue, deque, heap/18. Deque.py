class Deque:

    def __init__(self):
        self.deque = []

    def size(self):
        print(len(self.deque))

    def push_front(self, n: int):
        self.deque.insert(0, n)
        print('ok')

    def push_back(self, n: int):
        self.deque.append(n)
        print('ok')

    def pop_front(self):
        if len(self.deque) == 0:
            print('error')
            return
        print(self.deque.pop(0))

    def pop_back(self):
        if len(self.deque) == 0:
            print('error')
            return
        print(self.deque.pop())

    def front(self):
        if len(self.deque) == 0:
            print('error')
            return
        print(self.deque[0])

    def back(self):
        if len(self.deque) == 0:
            print('error')
            return
        print(self.deque[-1])

    def clear(self):
        self.deque.clear()
        print('ok')

    @staticmethod
    def exit():
        print('bye')


def handler():
    deque = Deque()
    flag = True
    while flag:
        s = input().strip().split()
        cmd = s[0]
        if cmd == 'push_front':
            n = int(s[1])
            deque.push_front(n)
        elif cmd == 'push_back':
            n = int(s[1])
            deque.push_back(n)
        elif cmd == 'pop_front':
            deque.pop_front()
        elif cmd == 'pop_back':
            deque.pop_back()
        elif cmd == 'front':
            deque.front()
        elif cmd == 'back':
            deque.back()
        elif cmd == 'size':
            deque.size()
        elif cmd == 'clear':
            deque.clear()
        elif cmd == 'exit':
            deque.exit()
            flag = False


handler()
