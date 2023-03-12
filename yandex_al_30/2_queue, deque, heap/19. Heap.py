class HeapMax:

    def __init__(self):
        self.heap = []

    def insert(self, k: int):
        self.heap.append(k)
        pos = len(self.heap) - 1

        while pos > 0 and self.heap[pos] > self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = self.heap[(pos - 1) // 2], self.heap[pos]
            pos = (pos - 1) // 2

    def extract(self) -> int:
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        pos = 0

        while pos * 2 + 2 < len(self.heap):
            max_son_pos = pos * 2 + 1
            if self.heap[max_son_pos] < self.heap[pos * 2 + 2]:
                max_son_pos = pos * 2 + 2

            if self.heap[pos] < self.heap[max_son_pos]:
                self.heap[pos], self.heap[max_son_pos] = self.heap[max_son_pos], self.heap[pos]
                pos = max_son_pos
            else:
                break

        self.heap.pop()
        return ans


n = int(input().strip())

heap = HeapMax()
for _ in range(n):
    s = list(map(int, input().strip().split()))
    if s[0] == 0:
        heap.insert(s[1])
    else:
        print(heap.extract())
