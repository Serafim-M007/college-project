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

def insertion_sort(arr, show_steps=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            if show_steps:
                show(i - j, j)  # gap = distance from the key to the item being compared
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = insertion_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Insertion Sort: {elapsed:.4f} s   correct: {result == expected}")


##1 Menit 37 detik