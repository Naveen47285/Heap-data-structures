import time
import random
from heapsort import heapsort


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def test_algorithms():
    sizes = [1000, 5000, 10000]

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        print(f"\nDataset size: {size}")

        start = time.time()
        heapsort(arr.copy())
        print("HeapSort:", time.time() - start)

        start = time.time()
        quicksort(arr.copy())
        print("QuickSort:", time.time() - start)

        start = time.time()
        merge_sort(arr.copy())
        print("MergeSort:", time.time() - start)


if __name__ == "__main__":
    test_algorithms()