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

def shell_sort(arr, show_steps=False):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                if show_steps:
                    show(gap, j)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

if __name__ == "__main__":
    numbers = read_numbers("random100K.txt")
    expected = sorted(numbers)
    data = numbers[:]

    start = time.perf_counter()
    result = shell_sort(data, SHOW_STEPS)
    elapsed = time.perf_counter() - start

    if SHOW_STEPS:
        print()
    print(f"Shell Sort: {elapsed:.4f} s   correct: {result == expected}")


##0,1718 detik