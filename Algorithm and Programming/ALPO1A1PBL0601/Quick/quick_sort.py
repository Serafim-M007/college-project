import time

def show_step(text, delay):
    # \r moves the cursor back to the start of the line, so each new message overwrites the last one
    print(f"\r{text:<60}", end="", flush=True)
    time.sleep(delay)

def partition(arr, low, high, delay):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                show_step(f"Moving {arr[i]} to index {i}", delay)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    show_step(f"Pivot {pivot} placed at index {i + 1}", delay)
    return i + 1

def quick_sort(arr, delay, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high, delay)
        quick_sort(arr, delay, low, p - 1)
        quick_sort(arr, delay, p + 1, high)

numbers = [98, 254, 344, 171, 13, 19, 44, 366, 108, 515, 173, 91, 480, 217, 927, 445, 119, 807, 122, 819, 749, 679, 185, 899, 955, 791, 476, 564, 241, 469, 488, 695, 155, 371, 752, 130, 657, 553, 615, 90, 487, 770, 528, 406, 406, 615, 180, 400, 692, 679]

quick_sort(numbers, delay=0.05)
print()
print("Final:", numbers)