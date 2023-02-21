class HeapMin:

    def __init__(self):
        self.heap = []

    def insert(self, k: int):
        self.heap.append(k)
        pos = len(self.heap) - 1

        while pos > 0 and self.heap[pos] < self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = self.heap[(pos - 1) // 2], self.heap[pos]
            pos = (pos - 1) // 2

    def extract(self) -> int:
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        pos = 0

        while pos * 2 + 2 < len(self.heap):
            min_son_pos = pos * 2 + 1
            if self.heap[min_son_pos] > self.heap[pos * 2 + 2]:
                min_son_pos = pos * 2 + 2

            if self.heap[pos] > self.heap[min_son_pos]:
                self.heap[pos], self.heap[min_son_pos] = self.heap[min_son_pos], self.heap[pos]
                pos = min_son_pos
            else:
                break

        self.heap.pop()
        return ans


def heap_sort(arr: list) -> list:
    ans = []
    heap = HeapMin()
    for i in range(len(arr)):
        heap.insert(arr[i])

    for _ in range(len(arr)):
        ans.append(heap.extract())

    return ans


input()
arr = list(map(int, input().strip().split()))
print(*heap_sort(arr))
