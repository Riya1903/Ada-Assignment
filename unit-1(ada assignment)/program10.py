class Heap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        minimum = self.heap.pop()
        self._heapify_down(0)
        return minimum

    def build_heap(self, lst):
        self.heap = lst
        for i in range(len(lst) // 2, -1, -1):
            self._heapify_down(i)

def heap_sort(lst):
    heap = Heap()
    heap.build_heap(lst)
    sorted_lst = []
    while True:
        minimum = heap.extract_min()
        if minimum is None:
            break
        sorted_lst.append(minimum)
    return sorted_lst

# Example usage:
lst = [9, 2, 5, 1, 7, 3]
sorted_lst = heap_sort(lst)
print("Sorted list:", sorted_lst)
