import time

SHOW_STEPS = False  # True: print "Gap n, Index n" while sorting (very slow on 100K)
STEP_DELAY = 0      # pause between printed steps, used only when SHOW_STEPS is True

def read_numbers(filename):
    with open(filename) as f:
        return [int(line) for line in f if line.strip()]

def show(gap, index):
    print(f"\rGap {gap}, Index {index}      ", end="", flush=True)
    if STEP_DELAY:
        time.sleep(STEP_DELAY)

def bubble_sort(arr, show_steps=False):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if show_steps:
                show(1, j)  # comparing neighbors, so the gap is 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = bubble_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Bubble Sort: {elapsed:.4f} s   correct: {result == expected}")

### 4 menit