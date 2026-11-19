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

def merge(arr, lo, mid, hi, show_steps):
    left = arr[lo:mid + 1]
    right = arr[mid + 1:hi + 1]
    gap = hi - lo + 1  # gap = size of the section being merged
    i = j = 0
    k = lo

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        if show_steps:
            show(gap, k)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        if show_steps:
            show(gap, k)
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        if show_steps:
            show(gap, k)
        k += 1

def merge_sort(arr, show_steps=False, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort(arr, show_steps, lo, mid)
        merge_sort(arr, show_steps, mid + 1, hi)
        merge(arr, lo, mid, hi, show_steps)
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = merge_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Merge Sort: {elapsed:.4f} s   correct: {result == expected}")


##0,1222 detik