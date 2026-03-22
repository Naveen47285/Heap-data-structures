class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)

        return root

    def increase_key(self, index, new_priority):
        if new_priority < self.heap[index].priority:
            return

        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i].priority > self.heap[parent].priority:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        n = len(self.heap)
        largest = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)