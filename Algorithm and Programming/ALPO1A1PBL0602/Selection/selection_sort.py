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

def selection_sort(arr, show_steps=False):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if show_steps:
                show(j - min_idx, j)  # gap = distance from the current minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = selection_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Selection Sort: {elapsed:.4f} s   correct: {result == expected}")


##1 Menit 53 detik