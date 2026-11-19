import time
import random

SHOW_STEPS = False  # True: print "Gap n, Index n" while sorting (very slow on 100K)
STEP_DELAY = 0      # pause between printed steps, used only when SHOW_STEPS is True

def read_numbers(filename):
    with open(filename) as f:
        return [int(line) for line in f if line.strip()]

def show(gap, index):
    print(f"\rGap {gap}, Index {index}      ", end="", flush=True)
    if STEP_DELAY:
        time.sleep(STEP_DELAY)

def partition(arr, low, high, show_steps):
    # Random pivot: avoids the slow case when the data is already ordered
    r = random.randint(low, high)
    arr[r], arr[low] = arr[low], arr[r]
    pivot = arr[low]

    # Three-way partition: items < pivot go left, items > pivot go right,
    # and items equal to the pivot stay in the middle (handles repeated values)
    lt, i, gt = low, low + 1, high
    gap = high - low  # gap = size of the section being partitioned
    while i <= gt:
        if show_steps:
            show(gap, i)
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def quick_sort(arr, show_steps=False, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low < high:
        lt, gt = partition(arr, low, high, show_steps)
        # Recurse into the smaller side and loop on the larger side,
        # which keeps the recursion depth small
        if lt - low < high - gt:
            quick_sort(arr, show_steps, low, lt - 1)
            low = gt + 1
        else:
            quick_sort(arr, show_steps, gt + 1, high)
            high = lt - 1
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = quick_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Quick Sort: {elapsed:.4f} s   correct: {result == expected}")


###0,0838 detik