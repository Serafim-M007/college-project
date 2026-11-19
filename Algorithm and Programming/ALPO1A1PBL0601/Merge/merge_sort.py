import time

def show_step(text, delay):
    print(f"\r{text:<60}", end="", flush=True)
    time.sleep(delay)

def merge(arr, lo, mid, hi, delay):
    left = arr[lo:mid + 1]
    right = arr[mid + 1:hi + 1]
    i = j = 0
    k = lo

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            value = left[i]
            i += 1
        else:
            value = right[j]
            j += 1
        arr[k] = value
        show_step(f"Placing {value} at index {k}", delay)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        show_step(f"Placing {left[i]} at index {k}", delay)
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        show_step(f"Placing {right[j]} at index {k}", delay)
        j += 1
        k += 1

def merge_sort(arr, delay, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort(arr, delay, lo, mid)
        merge_sort(arr, delay, mid + 1, hi)
        merge(arr, lo, mid, hi, delay)

numbers = [98, 254, 344, 171, 13, 19, 44, 366, 108, 515, 173, 91, 480, 217, 927, 445, 119, 807, 122, 819, 749, 679, 185, 899, 955, 791, 476, 564, 241, 469, 488, 695, 155, 371, 752, 130, 657, 553, 615, 90, 487, 770, 528, 406, 406, 615, 180, 400, 692, 679]

merge_sort(numbers, delay=0.05)
print()
print("Final:", numbers)