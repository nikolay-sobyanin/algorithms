class Queue:

    def __init__(self):
        self.queue = []

    def size(self):
        print(len(self.queue))

    def push(self, n: int):
        self.queue.append(n)
        print('ok')

    def pop(self):
        if len(self.queue) == 0:
            print('error')
            return
        print(self.queue.pop(0))

    def front(self):
        if len(self.queue) == 0:
            print('error')
            return
        print(self.queue[0])

    def clear(self):
        self.queue.clear()
        print('ok')

    @staticmethod
    def exit():
        print('bye')


def handler():
    queue = Queue()
    flag = True
    while flag:
        s = input().strip().split()
        cmd = s[0]
        if cmd == 'push':
            n = int(s[1])
            queue.push(n)
        elif cmd == 'pop':
            queue.pop()
        elif cmd == 'front':
            queue.front()
        elif cmd == 'size':
            queue.size()
        elif cmd == 'clear':
            queue.clear()
        elif cmd == 'exit':
            queue.exit()
            flag = False


handler()
