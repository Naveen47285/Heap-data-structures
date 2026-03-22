from priority_queue import PriorityQueue, Task


def simulate_scheduler():
    pq = PriorityQueue()

    tasks = [
        Task(1, 3),
        Task(2, 5),
        Task(3, 1),
        Task(4, 4)
    ]

    for task in tasks:
        pq.insert(task)

    print("Task execution order (highest priority first):")

    while not pq.is_empty():
        print(pq.extract_max())


if __name__ == "__main__":
    simulate_scheduler()